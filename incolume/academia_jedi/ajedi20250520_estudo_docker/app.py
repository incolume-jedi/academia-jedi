# app.py (Exemplo simples com Flask)
from flask import Flask
import os
import psycopg2
import redis

app = Flask(__name__)

# Configuração de banco de dados
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@db:5432/mydatabase")
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("Conectado ao PostgreSQL com sucesso!")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

# Configuração do Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    r.ping()
    print("Conectado ao Redis com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao Redis: {e}")


@app.route('/')
def hello_world():
    return 'Olá do Docker Compose com Python, PostgreSQL e Redis!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
