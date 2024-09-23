import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) != 2:
    print("Uso: python seumodulo.py <numero_pedido>")
    sys.exit(1)
numero_pedido = sys.argv[1]

service = Service("/usr/local/bin/geckodriver")
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(service=service, options=options)

print("Iniciando login...")

driver.get("https://pedidoeletronico.servimed.com.br/login")

username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = driver.find_element(By.NAME, 'password')
username_field.send_keys("juliano@farmaprevonline.com.br")
password_field.send_keys("a007299A")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/ng-component/div/div/form/button")))
login_button.click()

time.sleep(5)

print("Login efetuado com sucesso.")
print("Navegando para a página 'Meus Pedidos'...")

driver.get("https://pedidoeletronico.servimed.com.br/pedidos")

campo_pesquisa = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.form-control:nth-child(1)')))
campo_pesquisa.send_keys(numero_pedido)

botao_pesquisar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.row:nth-child(2) > div:nth-child(2) > button:nth-child(1)')))
botao_pesquisar.click()

print(f"Procurando o pedido {numero_pedido}...")


lupa_detalhes = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-icon > i:nth-child(1)')))
lupa_detalhes.click()

time.sleep(5) 

try:
    print("Capturando os dados do pedido...")
    
    pedido_encontrado = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-body')))
    
    if pedido_encontrado:    
        itens_pedido = []
        #  localizar o campo "Motivo da Rejeição"
        try:
            motivo = driver.find_element(By.CSS_SELECTOR, 'div.col-md-4:nth-child(4) > div:nth-child(1) > input:nth-child(2)').get_attribute('value')
        except:
            motivo = None 
        
        produtos = driver.find_elements(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr')

        # itera sobre cada produto e captura os dados
        for produto in produtos:
            codigo_produto = produto.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text  # Captura o código do produto
            descricao = produto.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text  # Captura a descrição do produto
            quantidade_faturada = produto.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text  # Captura a quantidade faturada

            # adc os dados do produto à lista de itens
            itens_pedido.append({
                "codigo_produto": codigo_produto,
                "descricao": descricao,
                "quantidade_faturada": quantidade_faturada
            })

        #  dicionário final com os dados do pedido
        dados_pedido = {
            "motivo-rejeicao": motivo,
            "itens": itens_pedido
        }

        print("Dados do pedido capturados com sucesso.")

        output_file = '/usr/src/app/output/dados_pedido.json'
        with open(output_file, 'w') as arquivo_json:
            json.dump(dados_pedido, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados do pedido salvos no arquivo {output_file}.")

except Exception as e:
    print(f"Ocorreu um erro ao tentar capturar os dados: {e}")

driver.quit()
print("Fim do script.")