from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

ZAPI_TOKEN = "FE159CBD3E314AC8890DBA72"
ZAPI_INSTANCE_ID = "3E53AE16CC18B190D85F2AC1CE4E084C"

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    try:
        message = data.get("text")
        phone = data.get("phone")

        if message and phone:
            resposta = f"Olá! Recebemos sua mensagem às {datetime.now().strftime('%H:%M:%S')} — já vamos te ajudar."
            send_message(phone, resposta)

    except Exception as e:
        print("Erro ao processar mensagem:", e)

    return jsonify({"status": "ok"})

def send_message(phone, message):
    url = f"https://api-whatsapp.wascript.com.br/send-message"
    headers = {
        "Content-Type": "application/json",
        "apikey": ZAPI_TOKEN,
        "instanceid": ZAPI_INSTANCE_ID
    }
    payload = {
        "phone": phone,
        "message": message
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Resposta da API Z-API:", response.text)
