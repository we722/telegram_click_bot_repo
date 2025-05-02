# Telegram Click Bot with Flask

## Features
- Telegram Bot integration with `/start` and `/stat` commands
- Flask backend with `/click` API and `/webhook/<TOKEN>` route
- Clicks tracked per user, saved in `users.json`
- Environment-variable-based config (BOT_TOKEN, ADS_LINK)
- Ready to deploy on Render with Procfile & requirements.txt

## Environment Variables
- `BOT_TOKEN` (required): Your Telegram Bot Token
- `ADS_LINK` (optional): Link opened when user clicks earn button

## Deployment
1. Upload code to GitHub
2. Connect Render to GitHub repo
3. Set Environment Variables in Render Dashboard
4. Set Telegram Bot Webhook:
```
https://<your-render-url>/webhook/<your-bot-token>
```

## Usage
- `/start`: Get earn button
- `/stat`: View your click count
- Use `/click` API to register clicks
