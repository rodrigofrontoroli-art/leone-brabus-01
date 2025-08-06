from flask import Flask, request, jsonify
import openai
import os
from datetime import datetime

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    mensagem_usuario = data.get("message", "Olá!")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é Leone, o corretor virtual da Brabus Negócios Imobiliários. Atenda de forma consultiva e personalizada."},
                {"role": "user", "content": mensagem_usuario}
            ],
            temperature=0.7
        )

        texto_resposta = resposta["choices"][0]["message"]["content"]
        agora = datetime.now().strftime("%H:%M:%S")
        resposta_final = f"[{agora}] {texto_resposta}"
        return jsonify({"reply": resposta_final})

    except Exception as e:
        return jsonify({"error": str(e)}), 500