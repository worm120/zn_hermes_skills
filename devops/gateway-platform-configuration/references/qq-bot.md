# QQ Bot Gateway Setup (Official API v2)

QQ Bot is a supported Hermes Gateway platform. The adapter lives at `gateway/platforms/qqbot/` and connects via the QQ Official Bot API v2 WebSocket gateway.

## Prerequisites

1. Register a bot at [QQ Open Platform (q.qq.com)](https://q.qq.com) — get **App ID** and **Client Secret**
2. Enable the **QQ Bot** capability for the app
3. Install Python dependency:
   ```bash
   ~/.hermes/hermes-agent/venv/bin/python3 -m pip install aiohttp
   ```

## Configuration

### Option A: Via .env (simplest)

Add to `~/.hermes/.env`:
```bash
QQ_APP_ID=your_app_id
QQ_CLIENT_SECRET=your_client_secret
QQ_ALLOW_ALL_USERS=true
```

### Option B: Via config.yaml

Add to `~/.hermes/config.yaml`:
```yaml
platforms:
  qq:
    enabled: true
    type: qqbot
    extra:
      app_id: "your_app_id"
      client_secret: "your_client_secret"
      markdown_support: true           # Enable QQ Markdown messages
      dm_policy: "open"                # open | allowlist | disabled
      allow_from: ["openid_1"]         # DM whitelist (if dm_policy=allowlist)
      group_policy: "open"             # open | allowlist | disabled
      group_allow_from: ["group_openid_1"]  # Group whitelist
```

### Both work; the adapter reads config.yaml `extra` first, then falls back to env vars.

## Verification

```python
from gateway.platforms.qqbot import QQAdapter, check_qq_requirements
print(f"Requirements met: {check_qq_requirements()}")
# → Should print True
```

## Starting the Gateway

```bash
hermes gateway run
```

Check the logs for connection status:
```bash
grep qqbot ~/.hermes/logs/gateway.log
```

Expected successful connection log:
```
[QQBot:<app_id>] WebSocket connected to wss://api.sgroup.qq.com/websocket
[QQBot:<app_id>] Connected
[QQBot:<app_id>] Ready, session_id=...
✓ qqbot connected
```

## Voice Transcription (STT)

The adapter supports voice-to-text for voice messages. Priority:
1. **QQ's built-in `asr_refer_text`** (free, always tried first)
2. **Configured STT provider** via `stt` config block

Config example for third-party STT:
```yaml
platforms:
  qq:
    extra:
      stt:
        provider: "zai"         # zai (GLM-ASR), openai (Whisper), etc.
        baseUrl: "https://open.bigmodel.cn/api/coding/paas/v4"
        apiKey: "your-key"
        model: "glm-asr"
```

## Technical Details

| Property | Value |
|----------|-------|
| API Base | `https://api.sgroup.qq.com` |
| Token URL | `https://bots.qq.com/app/getAppAccessToken` |
| WebSocket | `wss://api.sgroup.qq.com/websocket` |
| Message limit | 4000 chars |
| Message types | Text (0), Markdown (2), Media (7) |
| Media types | Image (1), Video (2), Voice (3), File (4) |
| Reconnect strategy | Exponential backoff: 2s → 5s → 10s → 30s → 60s |
| Max reconnect attempts | 100 |

## NixOS Note

On NixOS, you must set `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` in `~/.hermes/.env`:
```bash
SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```
Otherwise Python SSL context fails with `SSLCertVerificationError` when connecting to `api.sgroup.qq.com`.
