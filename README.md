# Portfólio Rosa — Projeto Integrado (DWS + POO + BD)

Portfólio pessoal de João Rosa com back-end em **Python/Flask (POO)** e banco **MySQL**.

## Etapa 2 — Back-end funcional

Estrutura em camadas:

| Pasta / arquivo | Função |
|---|---|
| `models/mensagem.py` | Classe `Mensagem` (atributos, validação, conversão para JSON) |
| `dao/mensagem_dao.py` | Classe `MensagemDAO`: inserir, listar, buscar_por_id, atualizar, excluir |
| `routes/mensagem_routes.py` | Rotas Flask (Blueprint) do CRUD, respostas em JSON |
| `config/database.py` | Conexão com o MySQL |
| `app.py` | Ponto de entrada da aplicação |
| `banco.sql` | Criação do banco `portfolio_db` e da tabela `mensagens` |

As páginas `index.html`, `pages/sobre.html` e `pages/contato.php` (versão em PHP do CRUD) continuam no projeto. O front-end que consome a API via Fetch será feito na entrega final.

## Como rodar

1. Inicie o MySQL pelo XAMPP e execute o `banco.sql` (phpMyAdmin → Importar).
2. Instale as dependências:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
   pip install -r requirements.txt
   ```
3. Inicie a API:
   ```
   python app.py
   ```
4. A API fica em `http://127.0.0.1:5000`.

A conexão usa o padrão do XAMPP (`root`, sem senha). Para mudar, defina as variáveis `DB_HOST`, `DB_USER`, `DB_PASSWORD` e `DB_NAME`.

## Rotas

| Método | Rota | O que faz | Status |
|---|---|---|---|
| GET | `/api/mensagens` | Lista todas as mensagens | 200 |
| GET | `/api/mensagens/<id>` | Busca uma mensagem | 200 / 404 |
| POST | `/api/mensagens` | Cadastra (`nome`, `email`, `mensagem`) | 201 / 400 |
| PUT | `/api/mensagens/<id>` | Edita o texto (`mensagem`) | 200 / 400 / 404 |
| DELETE | `/api/mensagens/<id>` | Exclui | 200 / 404 |

Exemplo:
```
curl -X POST http://127.0.0.1:5000/api/mensagens -H "Content-Type: application/json" -d "{\"nome\":\"Ana\",\"email\":\"ana@x.com\",\"mensagem\":\"Oi!\"}"
```
