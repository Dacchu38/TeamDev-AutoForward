# TeamDev Auto-Forward Bot — v1.1.0

Personal Telegram auto-forward bot.

---

## Project Structure

```
TeamDev/
├── ignite.py
├── environ.py
├── requirements.txt
├── .env
│
├── core/
│   ├── herald.py
│   ├── conductor.py
│   ├── cmds.py
│   ├── guardian.py
│   └── logger.py
│
├── relay/
│   ├── engine.py
│   ├── throttle.py
│   ├── shifter.py
│   └── errors.py
│
├── vault/
│   └── store.py
│
└── wire/
    ├── glyph.py
    └── panel.py
```

---

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python ignite.py
```

### .env

| Key | Description |
|---|---|
| `API_ID` | From https://my.telegram.org |
| `API_HASH` | From https://my.telegram.org |
| `BOT_TOKEN` | From @BotFather |
| `OWNER_ID` | Your Telegram user ID |
| `MONGO_URI` | MongoDB Atlas connection string |
| `LOG_CHANNEL` | Channel/group for action logs (optional) |
| `RATE_LIMIT` | Global max msgs/min per pipeline (default: 20) |
| `WORKERS` | Concurrent forward workers (default: 4) |

---

## Anti-Flood Architecture

```
Channel message
     |
  engine.py           ← catch-all listener
     |
  throttle.py         ← enqueue (drops if full)
     |
  Queue (per pipeline)
     |
  Worker pool         ← WORKERS concurrent workers
     |                   round-robin drain
  Token Bucket        ← per-pipeline rate limit (msgs/min)
     |
  Delay               ← configurable sleep between targets
     |
  shifter.py          ← forward with retry
     |
  errors.py           ← FloodWait / retry / backoff / permanent error detection
```

**FloodWait**: when Telegram issues a wait, a global gate pauses ALL pipelines until it clears. No message is dropped — it stays in the queue.

---

## Pipeline Features

| Feature | Description |
|---|---|
| Source | 1 channel to watch |
| Targets | Unlimited channels/groups |
| Hide Tag | Remove "Forwarded from" label |
| Media Filter | all / text / photo / video / document / audio |
| Delay | Seconds between each target (default: 1.5s) |
| Rate Limit | Max msgs/min per pipeline (token bucket) |
| Keywords | Whitelist — forward only matching messages |
| Blacklist | Skip messages containing these words |
| Caption | prepend / append / replace caption text |
| Schedule | Active hours only with timezone |
| Dedup | Skip already-forwarded messages (7-day window) |
| Fwd Limit | Auto-pause after N forwards |
| Export | Download pipeline config as JSON |
| Stats | forwarded / skipped / deduped / errors |

---

## Custom Commands

### Simple
```
/add_cmd hello <b>Hello World!</b>
```

### Full JSON (reply to message)
```
/add_cmd
```
Reply to a message containing:
```json
{
  "command": "hello",
  "text": "<b>Hello!</b>\nWelcome.",
  "parse_mode": "html",
  "photo": null,
  "video": null,
  "enabled": true,
  "buttons": [
    [{"text": "Website", "url": "https://example.com"}],
    [{"text": "Ping", "callback": "ping"}]
  ]
}
```

### Bulk import (reply to .json file)
```
/add_cmd
```
Reply to a `.json` file containing an array of command objects.

### Other commands
| Command | Description |
|---|---|
| `/cmds` | List all custom commands |
| `/del_cmd name` | Delete a command |
| `/cmd_schema` | Show JSON schema |

---

## Admin Permissions

| Permission | What it allows |
|---|---|
| `pipelines` | Create / manage own pipelines |
| `broadcast` | Send broadcast to all admins |
| `export` | Export pipeline configs |
| `commands` | Manage custom commands |

---

## Commands

| Command | Access |
|---|---|
| `/start` / `/menu` | Authorized users |
| `/pipes` | Authorized users |
| `/new` | Authorized users |
| `/stats` | Authorized users |
| `/help` | Authorized users |
| `/cmds` | Authorized users |
| `/add_cmd` | Authorized users |
| `/del_cmd` | Authorized users |
| `/cmd_schema` | Authorized users |
| `/admins` | Owner only |

---

## Notes

- Bot must be **admin** in source channel to read messages
- Bot must be **admin** in target channels/groups to post
- Default pipeline delay is `1.5s` - keeps forwarding safe from flood
