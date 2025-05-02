# Telegram Click Bot (Flask + Webhook)

A simple Telegram bot built with Python, Flask, and Webhook that gives users clickable earning links and tracks stats.

## Features

- Telegram Bot with `/start` and `/stat` commands
- Inline button for users to click and earn
- Tracks user clicks and total income
- Saves data in `users.json`
- Flask server handles webhooks and click API
- Deployment-ready for Render or other services

---

## Environment Variables

Set these environment variables in Render's Dashboard or a `.env` file:

- `BOT_TOKEN` — Your Telegram Bot Token
- `ADS_LINK` — The link users will click to earn
- `RENDER_EXTERNAL_HOSTNAME` — (Auto-set by Render)
- `PORT` — (Optional, default: 5000)

---

## File Structure
