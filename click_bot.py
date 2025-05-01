
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Click Bot is running!"

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    user_id = data.get("user_id")
    # Normally you'd save user data here
    return jsonify({"message": f"Click registered for user {user_id}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
