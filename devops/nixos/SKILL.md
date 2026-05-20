---
name: nixos
description: NixOS system administration — troubleshooting, desktop fixes, SSL, FHS apps, input method
metadata:
  tags: [nixos, linux, desktop, wayland, fcitx5, ssl, troubleshooting]
---

# NixOS System Administration

NixOS-specific troubleshooting patterns and fixes for desktop/workstation usage. Run on this host.

## NixOS Rebuild

```bash
# Standard rebuild
sudo nixos-rebuild switch --flake /etc/nixos#nixos_nuc

# With proxy (recommended when fetching dependencies)
sudo env http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 nixos-rebuild switch --flake /etc/nixos#nixos_nuc
```

## NixOS SSL Certificate Fix (Python)

**Problem**: Python SSL fails with `SSLCertVerificationError: self-signed certificate in certificate chain` on NixOS. This happens because NixOS does not set `SSL_CERT_FILE` globally, and Python's default cert store doesn't find the system bundle.

**Fix**: Set these environment variables (in `~/.hermes/.env` for Hermes, or globally):
```bash
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

The cert bundle lives at `/etc/ssl/certs/ca-certificates.crt` (symlink to `/etc/static/ssl/certs/ca-certificates.crt`).

## Fcitx5 + Wayland + FHS Sandbox Apps (WeChat fix)

**Problem**: NixOS configures fcitx5 with `waylandFrontend = true`, meaning KWin manages input method via the Wayland text-input protocol. This works for native Wayland apps (WezTerm, etc.) but **NOT for XWayland apps** (Electron apps, many containerized/bwrap'd apps).

WeChat (official Linux 4.x) runs via bubblewrap FHS sandbox and defaults to XWayland. Result: Chinese input method doesn't work.

**Diagnosis steps**:
1. Verify fcitx5 is running: `ps aux | grep fcitx5`, `fcitx5-remote` (returns 2 = running, no active IM)
2. Check if the app is on XWayland: `cat /proc/<pid>/environ | tr '\0' '\n' | grep DISPLAY` — if `DISPLAY=:0` is set alongside `WAYLAND_DISPLAY`, the app uses XWayland
3. Check env vars inside the process for fcitx2 variables: `cat /proc/<pid>/environ | tr '\0' '\n' | grep -i IM_MODULE\|XMODIFIERS`

**Fix**: Launch WeChat with these environment variables:
```bash
GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx SDL_IM_MODULE=fcitx ELECTRON_OZONE_PLATFORM_HINT=wayland wechat
```

Or create a desktop file override at `~/.local/share/applications/` with the env vars in the `Exec=` line:
```
Exec=env GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx SDL_IM_MODULE=fcitx ELECTRON_OZONE_PLATFORM_HINT=wayland wechat %U
```

**Key insight**: `waylandFrontend = true` means `GTK_IM_MODULE` and `QT_IM_MODULE` are NOT set globally. XWayland apps need these explicitly.

## Common NixOS Commands

| Command | Purpose |
|---------|---------|
| `nixos-rebuild switch --flake /etc/nixos#nixos_nuc` | Rebuild system |
| `home-manager --version` | Check Home Manager |
| `fcitx5-remote -r` | Reload fcitx5 config |
| `fcitx5-configtool` | GUI input method config |
| `cat /proc/<pid>/environ \| tr '\0' '\n'` | Check env vars of running process |
| `rg '^(font\|fixed\|menuFont)' ~/.config/kdeglobals` | Check Plasma font settings |
