
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZAPI_INSTANCE_ID = "3E53AE16CC18B190D85F2AC1CE4E084C"
ZAPI_TOKEN = "FE159CBD3E314AC8890DBA72"
ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-messages"

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    try:
        phone = data["phone"]
        message = data["message"]
        nome = data.get("senderName", "cliente")

        texto_resposta = f"Olá, {nome}! Aqui é o Leone da Brabus. Acabei de receber sua mensagem. Em instantes o Rodrigo vai te responder pessoalmente 😉"

        payload = {
            "phone": phone,
            "message": texto_resposta
        }

        response = requests.post(ZAPI_URL, json=payload)
        print("Resposta enviada:", response.text)

    except Exception as e:
        print("Erro ao processar mensagem:", str(e))

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
