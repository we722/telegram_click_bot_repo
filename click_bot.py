import logging
import json
import os
from flask import Flask, request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.ext import Defaults

TOKEN = os.getenv("BOT_TOKEN")
ADS_LINK = os.getenv("ADS_LINK", "https://example.com")
DATA_FILE = "users.json"

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"users": {}, "clicks": 0}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()
    data["users"][user_id] = data["users"].get(user_id, 0)
    save_data(data)

    keyboard = [[InlineKeyboardButton("Click to Earn", url=ADS_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below to earn points:", reply_markup=reply_markup)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_data()
    total_users = len(data["users"])
    total_clicks = data["clicks"]
    income = total_clicks * 0.01
    await update.message.reply_text(
        f"Total Users: {total_users}\nTotal Clicks: {total_clicks}\nEstimated Income: ${income:.2f}"
    )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stat", stats))
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook/{TOKEN}"
    )

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    request_data = request.get_data(as_text=True)
    update = Update.de_json(json.loads(request_data), bot)
    application.process_update(update)
    return "OK"

if __name__ == "__main__":
    main()
