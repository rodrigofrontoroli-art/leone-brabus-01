
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Mensagem recebida:", data)

    # Verifica se é uma mensagem recebida válida
    if 'text' in data.get('message', {}):
        resposta = {
            "replies": [
                {
                    "message": "Olá! Eu sou o Leone, corretor virtual da Brabus. Me diga: está procurando imóvel para morar ou para investir?"
                }
            ]
        }
        return jsonify(resposta)

    # Se não for uma mensagem válida, retorna vazio
    return jsonify({})
