"""Conexão com o banco de dados MySQL (XAMPP).

Os valores podem ser alterados por variáveis de ambiente; se elas não
existirem, valem os padrões do XAMPP (root sem senha).
"""
import os

import mysql.connector

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "portfolio_db"),
    "charset": "utf8mb4",
}


def get_connection():
    """Abre e devolve uma nova conexão com o banco."""
    return mysql.connector.connect(**DB_CONFIG)
