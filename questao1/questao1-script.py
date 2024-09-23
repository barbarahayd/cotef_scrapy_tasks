from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

options = Options()
options.headless = True

#  GeckoDriver

# start WebDriver do Firefox
driver = webdriver.Firefox(options=options)

categorias = [
    "https://www.compra-agora.com/loja/alimentos/800",
    "https://www.compra-agora.com/loja/bazar/344",
   "https://www.compra-agora.com/loja/bebidas/778",
   "https://www.compra-agora.com/loja/bomboniere/183",
   "https://www.compra-agora.com/loja/cuidados-pessoais/180",
   "https://www.compra-agora.com/loja/laticinios/771",
   "https://www.compra-agora.com/loja/naturais-e-nutricao/1399",
   "https://www.compra-agora.com/loja/pet/215",
   "https://www.compra-agora.com/loja/roupa-e-casa/179",
   "https://www.compra-agora.com/loja/sorvetes/258"
]

produtos = []

for categoria in categorias:
    driver.get(categoria)

    # espera - produto esteja visível na página
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.img-fluid")))

    # coleta dados dos produtos - itera sobre todos os produtos na página
    elementos_produtos = driver.find_elements(By.CSS_SELECTOR, "li.text-center")  # Seletor para cada produto
    for produto in elementos_produtos:    
        try:
            nome_produto = produto.find_element(By.CSS_SELECTOR, "img.img-fluid").get_attribute("title")
        except:
            nome_produto = "Nome não encontrado"        
        try:
            url_imagem = produto.find_element(By.CSS_SELECTOR, "img.img-fluid").get_attribute("src")
        except:
            url_imagem = "URL da imagem não encontrada"        
        try:
            marca_produto = produto.find_element(By.CSS_SELECTOR, "div.produto-marca.mb-1").text.strip()
        except:
            marca_produto = "Marca não encontrada"

        # adiciona os dados do produto à lista de produtos
        produtos.append({
            "nome": nome_produto,
            "url_imagem": url_imagem,
            "marca": marca_produto
        })

output_dir = "/usr/src/app/output"
os.makedirs(output_dir, exist_ok=True)

# salva os dados em JSON
with open(f"{output_dir}/produtos.json", "w") as file:
    json.dump(produtos, file, ensure_ascii=False, indent=4)

# fecha o navegador
driver.quit()