
# Telegram Click Bot

This is a simple Telegram bot with Flask + Webhook support. Deploy it on Render.com easily.

## Files

- `click_bot.py`: Main bot logic with webhook support.
- `requirements.txt`: Python dependencies.
- `Procfile`: For Render deployment.
- `users.json`: Stores user data (initially empty).

## Deployment (Render.com)

1. Fork/upload this repo to GitHub.
2. Go to [https://render.com](https://render.com) and create a new web service.
3. Connect your GitHub repo.
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python click_bot.py`
6. Set environment variables as needed (e.g., `BOT_TOKEN`, etc.)
7. Deploy!

Enjoy your working bot.
