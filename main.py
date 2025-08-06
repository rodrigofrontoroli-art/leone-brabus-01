
from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Leone Brabus está rodando! 🟢 ({now})"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
