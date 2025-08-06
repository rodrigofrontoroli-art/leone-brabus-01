
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZAPI_TOKEN = "FE159CBD3E314AC8890DBA72"
INSTANCE_ID = "3E53AE16CC18B190D85F2AC1CE4E084C"

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    try:
        phone = data['message'][0]['phone']
        url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
        payload = {
            "phone": phone,
            "message": "Olá! Aqui é o Leone, corretor virtual da Brabus. Posso te ajudar a encontrar seu imóvel ideal?"
        }
        r = requests.post(url, json=payload)
        print("Resposta enviada:", r.json())
    except Exception as e:
        print("Erro ao processar webhook:", e)

    return jsonify({"status": "ok"})
