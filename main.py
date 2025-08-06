
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json

        # Extraindo dados principais
        mensagem = data.get("message", {}).get("text", "").lower()
        nome = data.get("message", {}).get("from_name", "Cliente")
        numero = data.get("message", {}).get("from", "Sem número")

        print(f"Mensagem recebida de {nome} ({numero}): {mensagem}")

        # Resposta padrão
        resposta = f"Olá {nome}, tudo bem? Aqui é o Leone, corretor online da Brabus. Me conta: o que você está buscando hoje?"

        return jsonify({
            "replies": [resposta]
        })

    except Exception as e:
        print("Erro ao processar mensagem:", e)
        return jsonify({"status": "erro", "detalhe": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
