import os
from pymongo import MongoClient

def salvar_mongodb(dados):
    try:
        mongo_url = os.environ.get("MONGO_URL", "mongodb://mongo:27017")
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
