# ZENVORA COIN — starter bot

This is a first working prototype for Telegram virtual points (not cryptocurrency).

## Setup
1. Create a Python project on a hosting service that supports persistent files.
2. Upload `bot.py` and `requirements.txt`.
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables:
   - `BOT_TOKEN`: token from @BotFather (keep secret)
   - `ADMIN_ID`: your numeric Telegram user ID (optional; get it by messaging /id after starting the bot)
5. Run: `python bot.py`

## Included
- /start registration
- Wallet balance
- Daily Mining (+100 Z every 24 hours)
- Referral links (+200 virtual Z for a newly registered referred user)
- Leaderboard
- Basic admin statistics (/admin)

## Important
- Balances are stored in SQLite. Use persistent storage on the hosting service.
- Do not commit or share your bot token.
- This version has no blockchain, exchange, withdrawals, or cash value.
- Before public launch, add rate limits, stronger fraud controls, backups, privacy policy, and admin moderation.
