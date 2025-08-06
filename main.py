
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    mensagem = data.get('message', '')
    numero = data.get('phone', '')

    if mensagem and numero:
        resposta = "Olá! Aqui é o Leone Brabus. Como posso te ajudar a encontrar o imóvel ideal?"

        # Envia resposta automática
        requests.post("https://api-whatsapp.wascript.com.br/send-text", json={
            "instance_id": "3E53AE16CC18B190D85F2AC1CE4E084C",
            "access_token": "FE159CBD3E314AC8890DBA72",
            "phone": numero,
            "message": resposta
        })

    return jsonify({"status": "mensagem enviada"})
