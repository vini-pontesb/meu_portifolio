import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_url = os.environ.get('DATABASE_URL')
print(f"DATABASE_URL carregada: {db_url}")

try:
    print("Tentando conectar com psycopg2...")
    conn = psycopg2.connect(db_url, connect_timeout=10)
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")



