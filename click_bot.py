import logging
import json
import os
from flask import Flask, request, jsonify
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, Defaults

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

@app.route('/')
def home():
    return "Click Bot is running!"

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    user_id = data.get("user_id")
    db = load_data()
    db["clicks"] += 1
    db["users"][user_id] = db["users"].get(user_id, 0) + 1
    save_data(db)
    return jsonify({"message": f"Click registered for user {user_id}"}), 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    db = load_data()
    db["users"][user_id] = db["users"].get(user_id, 0)
    save_data(db)
    keyboard = [[InlineKeyboardButton("Click to Earn", url=ADS_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below to earn points:", reply_markup=reply_markup)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = load_data()
    total_users = len(db["users"])
    total_clicks = db["clicks"]
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
    from telegram import Bot
    bot = Bot(token=TOKEN)
    update = Update.de_json(json.loads(request.get_data(as_text=True)), bot)
    application = Application.builder().token(TOKEN).build()
    application.process_update(update)
    return "OK"

if __name__ == "__main__":
    main()
