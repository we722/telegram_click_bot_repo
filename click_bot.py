
from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Click Bot is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received:", data)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
