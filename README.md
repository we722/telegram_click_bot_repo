# Telegram Click Bot

## Features
- Telegram Bot Integration
- Flask Web Server
- Click Tracking
- Webhook Support
- Render Deployment Ready

## Setup Instructions

1. Set environment variables in Render dashboard:
   - `BOT_TOKEN`
   - `ADS_LINK`
   - (Optional) `PORT`

2. Deploy using Render:
   - Add your GitHub repo or upload this ZIP.
   - Render will auto-install from `requirements.txt`.
   - `Procfile` ensures Flask runs via Gunicorn.

3. Bot Commands:
   - `/start` - Show earning message
   - `/stat` - Show user's click count

Make sure `users.json` is present or it will be auto-created.