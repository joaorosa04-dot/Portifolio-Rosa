"""DAO (Data Access Object): único lugar que fala SQL com a tabela `mensagens`."""
from config.database import get_connection
from models.mensagem import Mensagem


class MensagemDAO:
    def inserir(self, msg):
        """Cadastra uma mensagem e devolve o id gerado."""
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO mensagens (nome, email, mensagem) VALUES (%s, %s, %s)",
                (msg.nome, msg.email, msg.mensagem),
            )
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def listar(self):
        """Devolve todas as mensagens, da mais nova para a mais antiga."""
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM mensagens ORDER BY data_envio DESC, id DESC")
            return [Mensagem.from_row(r) for r in cur.fetchall()]
        finally:
            conn.close()

    def buscar_por_id(self, id):
        """Devolve a Mensagem com esse id, ou None se não existir."""
        conn = get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT * FROM mensagens WHERE id = %s", (id,))
            row = cur.fetchone()
            return Mensagem.from_row(row) if row else None
        finally:
            conn.close()

    def atualizar(self, id, texto):
        """Muda o texto da mensagem. Devolve True se achou o registro."""
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE mensagens SET mensagem = %s WHERE id = %s", (texto, id))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def excluir(self, id):
        """Apaga a mensagem. Devolve True se achou o registro."""
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM mensagens WHERE id = %s", (id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()
