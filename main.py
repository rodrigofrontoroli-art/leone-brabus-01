from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Leone Brabus está rodando com sucesso!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
