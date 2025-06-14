import json
import pandas as pd

def salvar_json(dados, local_arquivo):
    with open(local_arquivo, "w", encoding = "utf-8") as arquivo:
        json.dump(dados, arquivo, indent = 4, ensure_ascii = False)

def salvar_csv(dados, local_arquivo):
    try:
        df = pd.DataFrame(dados)
        df.to_csv(local_arquivo, index=False, encoding="utf-8")
    except ImportError:
        print("Erro ao salvar arquivo CSV.")

def print_dataframe(local_arquivo, quantidade=5):
    try:
        df = pd.read_json(local_arquivo)
        print("\nAlgumas das citações salvas:")
        print(df.head(quantidade).to_string(index=False))
    except Exception as e:
        print(f"Erro ao tentar ler e exibir o arquivo JSON: {e}")
