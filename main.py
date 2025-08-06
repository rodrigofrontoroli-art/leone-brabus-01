from flask import Flask, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    try:
        message_info = data.get("message", {})
        text = message_info.get("text", {}).get("text", "").strip()
        phone = data.get("phone", "")
        name = data.get("name", "Cliente")

        if text:
            resposta = f"Oi {name}, tudo bem? Aqui é o Leone da Brabus! Recebi sua mensagem e já estou verificando a melhor opção para você."
            enviar_mensagem(phone, resposta)
    except Exception as e:
        print("Erro ao processar webhook:", str(e))

    return jsonify({"status": "ok"})

def enviar_mensagem(telefone, mensagem):
    url = f"https://api-whatsapp.wascript.com.br/send-message"
    payload = {
        "instance_id": ZAPI_INSTANCE,
        "token": ZAPI_TOKEN,
        "phone": telefone,
        "message": mensagem
    }
    try:
        response = requests.post(url, json=payload)
        print("Resposta da API:", response.text)
    except Exception as erro:
        print("Erro ao enviar mensagem:", erro)

if __name__ == "__main__":
    app.run()
