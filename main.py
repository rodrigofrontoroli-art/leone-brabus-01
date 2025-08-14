from flask import Flask, request, jsonify
import os
import openai
from datetime import datetime

app = Flask(__name__)

# API Key da OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-4o"  # Troque para "gpt-5-turbo" quando estiver disponível

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

        # Prompt consultivo do Leone
        system_prompt = f"""
Você é Leone, corretor de imóveis da Brabus Negócios Imobiliários. 
Seu papel é entender o perfil do cliente, gerar conexão e vender.
Seu estilo é consultivo, elegante, direto e com inteligência emocional.
Você vende studios para investidores, coberturas para HNWI e também imóveis de terceiros.
Se o cliente for objetivo, responda direto. Se for curioso, explique mais. 
Sempre pergunte região, metragem, valor e tipo (planta ou pronto).
Use linguagem natural e nobre, como um corretor de elite que entende de investimento.
"""

        user_prompt = f"{name} disse: {message}"

        # Chamada ao GPT
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