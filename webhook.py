from flask import Flask, request, jsonify
import openai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return "Leone Brabus está online!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        mensagem_usuario = data.get("message", "")

        if not mensagem_usuario:
            return jsonify({"error": "Mensagem não fornecida"}), 400

        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Você é Leone, o corretor virtual da Brabus Negócios Imobiliários. Seja sempre consultivo, educado, inteligente e objetivo nas respostas."
                },
                {
                    "role": "user",
                    "content": mensagem_usuario
                }
            ],
            temperature=0.7
        )

        conteudo = resposta["choices"][0]["message"]["content"]
        hora = datetime.now().strftime("%H:%M:%S")
        return jsonify({"reply": f"[{hora}] {conteudo}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500