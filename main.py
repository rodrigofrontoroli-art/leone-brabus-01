from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Mensagem recebida do cliente:", data)
    return jsonify({"status": "mensagem recebida"})

if __name__ == "__main__":
    app.run(debug=True)