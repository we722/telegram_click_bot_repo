# Telegram Click Bot with Flask Webhook

## Features
- Telegram bot with /start and /stat commands
- Flask server with `/` and `/click` API
- Webhook handler at `/webhook/<BOT_TOKEN>`
- JSON file-based user and click data storage
- Ready for Render deployment

## Setup

1. Set environment variables:
    - BOT_TOKEN
    - ADS_LINK (optional)
    - PORT (Render will assign this automatically)
    - RENDER_EXTERNAL_HOSTNAME (Render provides this)

2. Deploy to Render using GitHub

## License
MIT