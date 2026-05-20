---
name: gateway-platform-configuration
description: "Configure Hermes Gateway messaging platform adapters — env vars, config.yaml structure, dependency installation, and platform-specific quirks for less common platforms (QQ Bot, Yuanbao, Weixin, Feishu, etc.). Companion to the hermes-agent bundled skill."
version: 1.0.0
author: Hermes Agent
platforms: [linux, macos, nixos, windows]
metadata:
  hermes:
    tags: [hermes, gateway, messaging, setup, platforms, devops]
    related_skills: [hermes-agent]
---

# Gateway Platform Configuration

Configuring a Hermes Gateway messaging platform (QQ Bot, Yuanbao, Feishu, DingTalk, WeCom, Weixin, etc.) follows a consistent pattern. This skill covers the workflow and platform-specific details that the bundled `hermes-agent` skill's platform list omits.

> **Pitfall: the hermes-agent skill's platform list may be incomplete.** It lists Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Home Assistant, DingTalk, Feishu, WeCom, BlueBubbles (iMessage), Weixin (WeChat), API Server, and Webhooks — but NOT QQ Bot or Yuanbao, which ARE supported. Always check `gateway/platforms/` directory for all available adapters.

## General Workflow

### 1. Discover the platform adapter

```bash
ls ~/.hermes/hermes-agent/gateway/platforms/ | grep qq  # or the platform name
```

Each subdirectory contains:
- `adapter.py` — main adapter class and `check_qq_requirements()` function
- `constants.py` — API URLs, timeouts, message limits
- Docstring at top of `adapter.py` shows exact `config.yaml` structure

### 2. Identify required env vars and dependencies

Read the adapter's `__init__` method to find which env vars it reads (usually via `os.getenv("VAR_NAME")`). Check `hermes_cli/config.py` for the config definition (search for `VAR_NAME`).

Common pattern: the adapter reads from `config.yaml` `platforms.<name>.extra.*` first, then falls back to env vars.

Check Python dependencies:
```python
# Common QQ Bot dependencies
pip install aiohttp httpx
```

### 3. Configure env vars

Write to `~/.hermes/.env`:
```bash
PLATFORM_API_KEY=xxx
PLATFORM_SECRET=yyy
```

### 4. Configure config.yaml

Add a `platforms` section (or append to existing):
```yaml
platforms:
  platform_name:
    enabled: true
    type: platform_type
    extra:
      key: "value"
```

Verify with:
```bash
grep -A 10 "^platforms:" ~/.hermes/config.yaml
```

### 5. Start the gateway

```bash
hermes gateway run                # foreground
hermes gateway install && start   # background service
```

Monitor logs:
```bash
grep -i "connected\|error\|fail" ~/.hermes/logs/gateway.log | tail -20
```

## Platform-Specific References

See the `references/` directory for per-platform guides:
- `references/qq-bot.md` — QQ Bot (Official API v2) detailed setup

## Platform Access Control Policies

Most messaging platforms support one or more of these access policies. They go in the `extra` section of the platform config:

| Policy | Values | Description |
|--------|--------|-------------|
| `dm_policy` | `open`, `allowlist`, `disabled` | Who can DM the bot |
| `group_policy` | `open`, `allowlist`, `disabled` | Which groups can interact |
| `allow_from` | List of user IDs | Whitelist for DM |
| `group_allow_from` | List of group IDs | Whitelist for groups |

## Troubleshooting

### SSL Certificate Errors (NixOS / custom CA)

On NixOS, Python's SSL context may not find the system CA bundle. Symptoms:
```
SSLCertVerificationError: certificate verify failed: self-signed certificate in certificate chain
```

Fix: Set cert path in `~/.hermes/.env`:
```bash
SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

The exact path varies by distribution (`/etc/ssl/certs/ca-bundle.crt`, `/etc/pki/tls/certs/ca-bundle.crt`, etc.).

### Pip not found in Hermes venv

On minimal systems (NixOS, container images), the Hermes venv may lack pip:
```bash
~/.hermes/hermes-agent/venv/bin/python3 -m ensurepip --upgrade
```
Then install deps with:
```bash
~/.hermes/hermes-agent/venv/bin/python3 -m pip install <package>
```

### Gateway fails to connect

1. Check adapter-specific requirements (`check_qq_requirements()` or equivalent)
2. Verify env vars are set: `grep "^PLATFORM_" ~/.hermes/.env`
3. Check logs: `tail -30 ~/.hermes/logs/gateway.log`
4. Ensure the config.yaml `platforms.<name>.enabled` is `true`
