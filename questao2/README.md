# Questão 2: Captura de dados de faturamento no site Servimed

Este script interage com o site [Servimed](https://pedidoeletronico.servimed.com.br/) e captura os dados de faturamento de um pedido específico, passado como argumento.

## Instruções para execução

### Via Docker

A imagem Docker está disponível no Docker Hub: [questao2_image](https://hub.docker.com/repository/docker/barbarahp/questao2_image/).

1. Baixe a imagem Docker:
   ```bash
   docker pull barbarahp/questao2_image:latest
    ```
2. Execute o container passando o número do pedido como argumento Certifique-se de mapear corretamente a pasta local para o diretório output dentro do container, onde o arquivo JSON será gerado:

    ```bash
    docker run -v /caminho/para/diretorio/output:/usr/src/app/output barbarahp/questao2_image python questao2_script.py <numero_pedido>
    ```
3. O arquivo JSON contendo os dados de do pedido será gerado no diretório output.

### Localmente (Caso prefira executar o script Python diretamente):

### Requisitos
- Python 3.9 instalado. [Instale o Python](https://www.python.org/downloads/).
- GeckoDriver [Download do GeckoDriver](https://github.com/mozilla/geckodriver/releases).

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

3. Execute o script Python passando o número do pedido como argumento:
    ```bash
    python questao2_script.py <numero_do_pedido>
    ```

### Resultado
Um arquivo dados_pedido.json será gerado com os seguintes campos:
* Código do produto
* Descrição
* Quantidade faturada
* Motivo Rejeição (se cancelado)