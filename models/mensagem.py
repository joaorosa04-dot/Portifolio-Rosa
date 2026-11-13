"""Classe de modelo: representa uma linha da tabela `mensagens`."""


class Mensagem:
    def __init__(self, nome, email, mensagem, id=None, data_envio=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
        self.data_envio = data_envio

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "mensagem": self.mensagem,
            "data_envio": self.data_envio.isoformat() if self.data_envio else None,
        }

    @classmethod
    def from_row(cls, row):
        """Cria um objeto Mensagem a partir de uma linha (dict) do banco."""
        return cls(
            id=row["id"],
            nome=row["nome"],
            email=row["email"],
            mensagem=row["mensagem"],
            data_envio=row["data_envio"],
        )

    @classmethod
    def from_json(cls, dados):
        """Cria um objeto Mensagem a partir do JSON recebido na rota."""
        return cls(
            nome=(dados.get("nome") or "").strip(),
            email=(dados.get("email") or "").strip(),
            mensagem=(dados.get("mensagem") or "").strip(),
        )

    def validar(self):
        """Devolve uma lista de erros (vazia se estiver tudo certo)."""
        erros = []
        if not self.nome or len(self.nome) > 100:
            erros.append("nome é obrigatório e deve ter até 100 caracteres")
        if not self.email or "@" not in self.email or len(self.email) > 100:
            erros.append("email é obrigatório, deve ser válido e ter até 100 caracteres")
        if not self.mensagem:
            erros.append("mensagem é obrigatória")
        return erros
