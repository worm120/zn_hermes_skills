# WeChat + Fcitx5 Input Method on NixOS

## Environment

- NixOS with Plasma 6 (Wayland)
- fcitx5 + RIME (`luna_pinyin_simp`)
- `i18n.inputMethod.fcitx5.waylandFrontend = true`
- WeChat 4.1.1 official Linux (nixpkgs package)
- WeChat runs via bubblewrap FHS sandbox (`wechat-4.1.1.4-fhsenv-rootfs`)

## Root Cause

The NixOS config comment says it clearly:

```
# KDE Plasma 6 Wayland: 让 KWin 管理 fcitx5 输入法
# 此时 GTK_IM_MODULE/QT_IM_MODULE 不由 NixOS 全局设置（由 KWin 通过 text-input 协议转发）
```

- **Native Wayland apps** (WezTerm): use `zwp_text_input_v3` protocol → KWin forwards to fcitx5 via `zwp_input_method_manager_v1` → **works fine**
- **XWayland apps** (WeChat, Electron apps): don't use Wayland text-input protocol → need `GTK_IM_MODULE=fcitx`/`QT_IM_MODULE=fcitx`/`XMODIFIERS=@im=fcitx`

WeChat runs under **XWayland** (`DISPLAY=:0` alongside `WAYLAND_DISPLAY=wayland-0` in its process env).

## The bubblewrap FHS Sandbox

WeChat's bwrap wrapper:
1. Creates tmpfs on `/etc` and mounts FHS-specific config
2. Inherits parent env vars by default (bwrap does not strip env)
3. `/init` script does `source /etc/profile` (the FHS env's profile, NOT the host's)
4. The FHS `/etc/profile` does NOT set any fcitx/IM vars
5. `/run` is bind-mounted from host, so D-Bus session bus is accessible

**Key takeaway**: env vars ARE inherited through bwrap. The original problem was that `GTK_IM_MODULE` and `QT_IM_MODULE` were not set at all (by design of waylandFrontend=true).

## Env Vars Check (before fix)

```
$ cat /proc/<wechat-pid>/environ | tr '\0' '\n' | grep -iE "IM_MODULE|XMODIFIERS|WAYLAND|DISPLAY"
XMODIFIERS=@im=fcitx           # ← set (from host shell?)
WAYLAND_DISPLAY=wayland-0
DISPLAY=:0                     # ← WeChat uses XWayland
```

Missing: `GTK_IM_MODULE`, `QT_IM_MODULE`, `SDL_IM_MODULE`

## The Fix

```bash
GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx SDL_IM_MODULE=fcitx ELECTRON_OZONE_PLATFORM_HINT=wayland wechat
```

Or desktop file (`~/.local/share/applications/wechat-fcitx-fix.desktop`):

```desktop
[Desktop Entry]
Exec=env GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx SDL_IM_MODULE=fcitx ELECTRON_OZONE_PLATFORM_HINT=wayland wechat %U
```

After fix, process env shows all vars properly set:
```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
ELECTRON_OZONE_PLATFORM_HINT=wayland
```

## Alternative: Permanent NixOS Fix

Instead of per-app env vars, set globally in `/etc/nixos/configuration.nix`:

```nix
# Inside environment.sessionVariables
environment.sessionVariables = {
  GTK_IM_MODULE = "fcitx";
  QT_IM_MODULE = "fcitx";
  XMODIFIERS = "@im=fcitx";
  SDL_IM_MODULE = "fcitx";
};
```

**Caveat**: This may interfere with native Wayland apps that work correctly with the text-input protocol. Test before applying.
