import os
import json
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADS_LINK = os.environ.get("ADS_LINK", "https://example.com")
WEBHOOK_TOKEN = BOT_TOKEN

DATA_FILE = "users.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def send_message(chat_id, text, reply_markup=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    requests.post(url, json=payload)

@app.route("/")
def home():
    return "Click Bot is Running!"

@app.route("/webhook/" + WEBHOOK_TOKEN, methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        user_id = str(chat_id)
        text = update["message"].get("text", "")
        if text == "/start":
            data = load_data()
            if user_id not in data:
                data[user_id] = {"clicks": 0}
                save_data(data)
            send_message(chat_id, "Welcome! Click the button below to earn.", {
                "inline_keyboard": [[{"text": "Click to Earn", "url": ADS_LINK}]]
            })
        elif text == "/stat":
            data = load_data()
            clicks = data.get(user_id, {}).get("clicks", 0)
            total_users = len(data)
            send_message(chat_id, f"You have {clicks} clicks.\nTotal Users: {total_users}")
    return "ok"

@app.route("/click", methods=["POST"])
def click():
    user_id = request.json.get("user_id")
    if not user_id:
        return {"error": "Missing user_id"}, 400
    data = load_data()
    if user_id not in data:
        data[user_id] = {"clicks": 1}
    else:
        data[user_id]["clicks"] += 1
    save_data(data)
    return {"message": "Click counted", "clicks": data[user_id]["clicks"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
