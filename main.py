from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    # Verifica se é mensagem de texto
    try:
        message = data["messages"][0]
        number = message["from"]
        text = message["text"]["body"]
        
        resposta = f"Olá, tudo bem? Aqui é o Leone da Brabus. Recebi sua mensagem: '{text}' e estou à disposição para te ajudar!"

        url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
        payload = {
            "phone": number,
            "message": resposta
        }
        headers = {
            "Content-Type": "application/json"
        }

        requests.post(url, json=payload, headers=headers)

    except Exception as e:
        print("Erro ao responder:", e)

    return jsonify({"status": "mensagem processada"})