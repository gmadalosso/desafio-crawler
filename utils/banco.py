import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def detecta_ambiente():
    if os.path.exists("/.dockerenv"):
        return "docker"
    return "local"

def testar_conexao(mongo_url):
    try:
        cliente = MongoClient(mongo_url, serverSelectionTimeoutMS=3000)
        cliente.admin.command("ping")
        return True
    except ConnectionFailure:
        return False

def salvar_mongodb(dados):
    ambiente = detecta_ambiente()
    print(f"Acessando o banco de dados do ambiente: {ambiente}")

    mongo_url = os.getenv("MONGO_URL_DOCKER") if ambiente == "docker" else os.getenv("MONGO_URL_LOCAL")

    if not testar_conexao(mongo_url):
        print(f"Não foi possível conectar ao MongoDB em: {mongo_url}")
        return

    try:
        cliente = MongoClient(mongo_url)
        db = cliente["mongo_desafio"]
        colecao = db["quotes"]

        if dados:
            colecao.insert_many(dados)
            print(f"{len(dados)} citações inseridas no banco de dados.")
        else:
            print("Nenhum dado para inserir no banco de dados.")
    except Exception as e:
        print(f"Erro ao salvar no banco de dados: {e}")
