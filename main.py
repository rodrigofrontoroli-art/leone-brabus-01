from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

TOKEN = os.getenv("WAZZUP_TOKEN")
INSTANCE_ID = os.getenv("WAZZUP_INSTANCE_ID")

@app.route("/")
def home():
    return "Leone Brabus está online!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    try:
        phone = data["phone"]
        message = "Olá, aqui é o Leone da Brabus. Como posso te ajudar?"
        send_message(phone, message)
    except Exception as e:
        print("Erro ao responder:", e)
    return jsonify({"status": "ok"})

def send_message(phone, text):
    url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"
    payload = {
        "phone": phone,
        "message": text
    }
    response = requests.post(url, json=payload)
    print("Resposta da API:", response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
