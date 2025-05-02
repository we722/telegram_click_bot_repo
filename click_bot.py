import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADS_LINK = os.environ.get("ADS_LINK", "https://example.com")
users_file = "users.json"

if not os.path.exists(users_file):
    with open(users_file, "w") as f:
        json.dump({}, f)

def load_users():
    with open(users_file, "r") as f:
        return json.load(f)

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f)

@app.route("/")
def home():
    return "Telegram Click Bot is Running!"

@app.route("/click", methods=["POST"])
def click():
    data = request.json
    user_id = str(data.get("user_id"))
    users = load_users()
    if user_id not in users:
        users[user_id] = {"clicks": 0}
    users[user_id]["clicks"] += 1
    save_users(users)
    return jsonify({"message": "Click recorded", "clicks": users[user_id]["clicks"]})

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.json
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        if text == "/start":
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                          json={"chat_id": chat_id,
                                "text": f"Welcome! Click the button below to earn.
{ADS_LINK}"})
        elif text == "/stat":
            users = load_users()
            total_users = len(users)
            clicks = users.get(str(chat_id), {}).get("clicks", 0)
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                          json={"chat_id": chat_id,
                                "text": f"Your Clicks: {clicks}\nTotal Users: {total_users}"})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)