import os
from pymongo import MongoClient

def detecta_ambiente():
    if os.path.exists("/.dockerenv"):
        return "docker"
    return "local"

def salvar_mongodb(dados):
    ambiente = detecta_ambiente()
    print(f"Acessando o bando de dados do ambiente: {ambiente}")

    try:
        if ambiente == "docker":
            mongo_url = os.getenv("MONGO_URL_DOCKER")
        else:
            mongo_url = os.getenv("MONGO_URL_LOCAL")

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
