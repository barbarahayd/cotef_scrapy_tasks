import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time
import argparse

# Função para configurar o WebDriver (Firefox)
def setup_driver():
    options = Options()
    options.headless = True  # Executa o Firefox no modo headless (sem abrir a janela)
    service = Service(executable_path='C:/geckodriver.exe')  #   informe o caminho correto do GeckoDriver
    driver = webdriver.Firefox(service=service, options=options)
    return driver

# Função para buscar todas as citações do autor em todas as páginas
def get_author_quotes(author_name):
    driver = setup_driver()
    
    # Dicionário para armazenar as informações da autora
    author_info = {
        "author": {
            "name": author_name,
            "birth_date": "",
            "birth_location": "",
            "description": ""
        },
        "quotes": []
    }
    
    page = 1
    while True:        
        url = f"http://quotes.toscrape.com/page/{page}/"
        driver.get(url)
        time.sleep(2)
        
        # verifica se a página existe (caso contrário, saímos do loop)
        if "No quotes found!" in driver.page_source:
            break
        
        # coletar todas as citações e tags na página atual
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            try:
                # procurar pelo nome da autora usando o seletor ".author"
                author = quote.find_element(By.CLASS_NAME, "author").text
                if author == author_name:
                    text = quote.find_element(By.CLASS_NAME, "text").text
                    tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
                    author_info["quotes"].append({
                        "text": text,
                        "tags": tags
                    })

                    # clicar no link "about" que contém o href específico (somente na primeira vez)
                    if not author_info["author"]["birth_date"]:
                        about_link = quote.find_element(By.XPATH, './/a[@href="/author/J-K-Rowling"]')
                        about_link.click()
                        time.sleep(2)

                        # extrai as informações da página "about"
                        birth_date = driver.find_element(By.CLASS_NAME, "author-born-date").text
                        birth_location = driver.find_element(By.CLASS_NAME, "author-born-location").text
                        description = driver.find_element(By.CLASS_NAME, "author-description").text

                        author_info["author"]["birth_date"] = birth_date
                        author_info["author"]["birth_location"] = birth_location
                        author_info["author"]["description"] = description.strip()

                        # voltar à página principal após acessar o "about"
                        driver.back()
                        time.sleep(2)

            except StaleElementReferenceException:
                # rebuscar o elemento se houver uma falha por causa de referência inválida
                quotes = driver.find_elements(By.CLASS_NAME, "quote")
        
        # ir para a próxima página
        page += 1

    # fechar o navegador
    driver.quit()

    # converte o dict para formato JSON e imprime na tela
    output_json = json.dumps(author_info, indent=4, ensure_ascii=False)
    print(output_json)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extrai citações e informações de autores do site quotes.toscrape.com')
    parser.add_argument('author_name', type=str, help='Nome do autor')
    args = parser.parse_args()

    get_author_quotes(args.author_name)