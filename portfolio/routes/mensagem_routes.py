"""Rotas Flask (Blueprint) do CRUD de mensagens. Todas respondem JSON."""
from flask import Blueprint, jsonify, request

from dao.mensagem_dao import MensagemDAO
from models.mensagem import Mensagem

mensagem_bp = Blueprint("mensagens", __name__, url_prefix="/api/mensagens")
dao = MensagemDAO()


def erro(texto, status):
    return jsonify({"erro": texto}), status


@mensagem_bp.route("", methods=["GET"])
def listar():
    mensagens = dao.listar()
    return jsonify([m.to_dict() for m in mensagens]), 200


@mensagem_bp.route("/<int:id>", methods=["GET"])
def buscar(id):
    msg = dao.buscar_por_id(id)
    if msg is None:
        return erro("mensagem não encontrada", 404)
    return jsonify(msg.to_dict()), 200


@mensagem_bp.route("", methods=["POST"])
def cadastrar():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return erro("envie um JSON válido", 400)

    msg = Mensagem.from_json(dados)
    erros = msg.validar()
    if erros:
        return jsonify({"erros": erros}), 400

    novo_id = dao.inserir(msg)
    return jsonify(dao.buscar_por_id(novo_id).to_dict()), 201


@mensagem_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return erro("envie um JSON válido", 400)

    texto = (dados.get("mensagem") or "").strip()
    if not texto:
        return erro("mensagem é obrigatória", 400)

    if not dao.atualizar(id, texto):
        return erro("mensagem não encontrada", 404)
    return jsonify(dao.buscar_por_id(id).to_dict()), 200


@mensagem_bp.route("/<int:id>", methods=["DELETE"])
def excluir(id):
    if not dao.excluir(id):
        return erro("mensagem não encontrada", 404)
    return jsonify({"mensagem": "excluída com sucesso"}), 200
