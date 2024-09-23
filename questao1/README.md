# Questão 1: Captura de dados de produtos no site Compra Agora
Este script interage com o site [Compra Agora](https://www.compra-agora.com) percorre cada categoria e captura os dados de todos os produtos disponíveis.

## Instruções para execução

### Via Docker
* A imagem Docker já está disponível no Docker Hub: [questao1_image](https://hub.docker.com/repository/docker/barbarahp/questao1_image/).
* Para executar o script via Docker, siga os passos abaixo:
  
1. Baixe a imagem Docker:
    ```bash
    docker pull barbarahp/questao1_image:latest
    ```
2. Execute o container:
    ```bash
    docker run -v /caminho/para/diretorio/local:/usr/src/app/output barbarahp/questao1_image:latest
    ```
3. O arquivo JSON contendo os dados será gerado no diretório `output`.


### Localmente (caso prefira executar o script Python diretamente)


### Requisitos
- Python 3.9 instalado. [Instale o Python](https://www.python.org/downloads/).
- GeckoDriver [Download do GeckoDriver](https://github.com/mozilla/geckodriver/releases).

O GeckoDriver é necessário para que o Selenium controle o navegador Firefox. Veja as instruções abaixo para baixar e configurar o GeckoDriver.

1. Instale as dependências:

    Utilize o pip para instalar as dependências listadas no arquivo requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```
2. Ajuste o caminho do GeckoDriver:

    Abra o arquivo Python e ajuste o caminho do GeckoDriver para apontar corretamente para o seu ambiente local:
    ```bash
    driver = webdriver.Firefox(executable_path='/caminho/para/geckodriver')
    ```

3. Execute o script:
    ```bash
    python questao1_script.py
    ```

### Resultado:
Um arquivo `produtos.json` com os seguintes campos:

  - Nome do produto
  - URL da imagem
  - Marca
