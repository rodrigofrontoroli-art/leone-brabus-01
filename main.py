from flask import Flask, request, jsonify
import os
import openai
from datetime import datetime

app = Flask(__name__)

# Configurações do GPT
openai.api_key = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-4o"  # Pode trocar para gpt-5-turbo quando estiver disponível via API

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"[{hora}] 📥 Mensagem recebida: {data}")

        message = data.get("text", "")
        phone = data.get("phone", "")
        name = data.get("name", "Cliente")

        # Prompt base para o Leone
        system_prompt = f"""
Você é Leone, corretor de imóveis da Brabus Negócios Imobiliários. 
Seu objetivo é atender leads de WhatsApp que chegam de anúncios de imóveis para venda ou investimento.
Você fala com elegância, é consultivo, entende perfil do cliente e sugere imóveis.
Use sempre linguagem natural, empática e personalizada, como um corretor humano de alto padrão.
Foque em venda, captação e qualificação. Se não tiver todas as respostas ainda, diga que irá verificar com a diretoria.
"""

        user_prompt = f"{name} disse: {message}"

        # Enviar para o GPT
        resposta = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        reply = resposta.choices[0].message['content']
        print(f"[{hora}] 🤖 Resposta Leone: {reply}")

        return jsonify({
            "messages": [
                {
                    "text": reply,
                    "phone": phone
                }
            ]
        }), 200

    except Exception as e:
        print("❌ Erro ao processar:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)