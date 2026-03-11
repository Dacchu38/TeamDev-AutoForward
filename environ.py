"""
                      [TeamDev](https://t.me/team_x_og)
          
          Project Id -> 30.
          Project Name -> TeamDev Auto-Forward
          Project Age -> 1Month+ (Updated On 11/03/2026)
          Project Idea By -> @MR_ARMAN_08
          Project Dev -> @MR_ARMAN_08
          Powered By -> @Team_X_Og ( On Telegram )
          Updates -> @CrimeZone_Update ( On telegram )
    
    Setup Guides -> Read > README.md
    
          This Script Part Off https://t.me/Team_X_Og's Team.
          Copyright ©️ 2026 TeamDev | @Team_X_Og
          
    • Some Quick Help
    - Read Full README.md For Understanding The Content.
    - If You Need Any Help Contact Us In @Team_X_Og's Group
    
         Compatible In BotApi 9.5 Fully
         Build For BotApi 9.5
         We'll Keep Update This Repo If We Got 30+ Stars In One Month Of Release.
"""

import os
from dotenv import load_dotenv

load_dotenv()

API_ID      = int(os.environ.get("API_ID", 0))
API_HASH    = os.environ.get("API_HASH", "")
BOT_TOKEN   = os.environ.get("BOT_TOKEN", "")
OWNER_ID    = int(os.environ.get("OWNER_ID", 0))
MONGO_URI   = os.environ.get("MONGO_URI", "")

_log_raw    = os.environ.get("LOG_CHANNEL", "").strip()
if _log_raw and not _log_raw.startswith("@") and not _log_raw.lstrip("-").isdigit():
    _log_raw = f"@{_log_raw}"
LOG_CHANNEL: str | None = _log_raw if _log_raw else None

RATE_LIMIT  = int(os.environ.get("RATE_LIMIT", "20"))
WORKERS     = int(os.environ.get("WORKERS", "4"))

FORCE_JOIN  = [c.strip() for c in os.environ.get("FORCE_JOIN", "").split(",") if c.strip()]

VERSION     = "1.1.0"

if not all([API_ID, API_HASH, BOT_TOKEN, OWNER_ID, MONGO_URI]):
    raise ValueError("[TeamDev Auto-Forward] Missing required env vars. Check .env file.")
