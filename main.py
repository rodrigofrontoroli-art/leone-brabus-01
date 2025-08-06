from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)

    try:
        mensagem = data['messages'][0]['text']['body']
        numero = data['messages'][0]['from']

        # Resposta personalizada
        resposta = f"Olá! Aqui é o Leone, corretor digital da Brabus. 👋\n\nRecebi sua mensagem: \"{mensagem}\"\nJá vou te ajudar com as melhores opções!"

        enviar_mensagem(numero, resposta)
    except Exception as e:
        print("Erro ao processar webhook:", e)

    return jsonify({"status": "mensagem recebida"})

def enviar_mensagem(numero, mensagem):
    url = "https://api-whatsapp.wascript.com.br/send-message"
    headers = {
        "Content-Type": "application/json",
        "apikey": "FE159CBD3E314AC8890DBA72"
    }

    payload = {
        "instance_id": "3E53AE16CC18B190D85F2AC1CE4E084C",
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(url, headers=headers, json=payload)
    print("Mensagem enviada. Status:", response.status_code)
    print("Resposta da API:", response.text)
