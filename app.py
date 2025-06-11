from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json
import time

def salvar_json(dados, local_arquivo):
    with open(local_arquivo, "w", encoding = "utf-8") as arquivo:
        json.dump(dados, arquivo, indent = 4, ensure_ascii = False)

def salvar_csv(dados, local_arquivo):
    try:
        df = pd.DataFrame(dados)
        df.to_csv(local_arquivo, index=False, encoding="utf-8")
    except ImportError:
        print("Erro ao salvar arquivo CSV.")


def main():
    URL = "http://quotes.toscrape.com"
    LOCAL_JSON = 'resultadosJSON/quotes.json'
    LOCAL_CSV = 'resultadosCSV/quotes.csv'

    resultados = []
    pagina = 1

    print("Iniciando raspagem dos dados...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    while True:
        print(f"Raspando página {pagina}...")

        time.sleep(1)

        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for q in quotes:
            texto = q.find_element(By.CLASS_NAME, "text").text
            autor = q.find_element(By.CLASS_NAME, "author").text
            tags = [tag.text for tag in q.find_elements(By.CLASS_NAME, "tag")]

            resultados.append({
                "texto": texto,
                "author": autor,
                "tags": tags
            })

        try:
            botao_proxima_pagina = driver.find_element(By.CSS_SELECTOR, ".next a")
            botao_proxima_pagina.click()
            pagina += 1
        except:
            print("Não há mais páginas. Finalizando raspagem.")
            break

        salvar_json(resultados, LOCAL_JSON)
        salvar_csv(resultados, LOCAL_CSV)

    print(f"Raspagem finalizada! {len(resultados)} citações salvas em '{LOCAL_JSON}' e '{LOCAL_CSV}'.")

    driver.quit()

if __name__ == "__main__":
    main()
