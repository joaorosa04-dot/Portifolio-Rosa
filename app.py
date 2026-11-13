"""Ponto de entrada do back-end Flask. Rode com: python app.py"""
from flask import Flask, jsonify

from routes.mensagem_routes import mensagem_bp

app = Flask(__name__)
app.register_blueprint(mensagem_bp)


@app.route("/")
def index():
    return jsonify({"status": "API do portfólio no ar", "rotas": "/api/mensagens"})


if __name__ == "__main__":
    app.run(debug=True)
