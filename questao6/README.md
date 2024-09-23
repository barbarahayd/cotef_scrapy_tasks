# Questão 6: Captura de Citações e Informações de "J.K. Rowling" com Selenium

Este script utiliza Selenium para acessar o site [quotes.toscrape.com](http://quotes.toscrape.com/), buscando todas as citações e tags da autora "J.K. Rowling". Além disso, o script clica no link "about" da autora e extrai informações adicionais (nome, data de nascimento, local de nascimento, e descrição sobre a autora). O resultado final é exibido no prompt no formato JSON.

## Instruções para execução

### Pré-requisitos

**GeckoDriver**:

  Certifique-se de ter o GeckoDriver instalado no seu sistema.

  No script, lembre-se de apontar o caminho correto para o GeckoDriver. No arquivo `questao6_script.py`, ajuste a linha:

  ```python
  driver = webdriver.Firefox(executable_path='CAMINHO_PARA_GECKODRIVER')
  ```
  Substitua `CAMINHO_PARA_GECKODRIVER` pelo caminho onde o GeckoDriver está localizado no seu sistema.

**Instale as dependências necessárias utilizando o comando abaixo:**
  ```python
  pip install -r requirements.txt
  ```

### Executar o script

1. Acesse a subpasta da questão 6:
   ```bash
   cd questao6
2. Execute o script passando o nome da autora "J.K. Rowling" como argumento:
    ```bash
    python questao6_script.py "J.K. Rowling"
    ```


### Resultado

O script exibirá o resultado no terminal em formato JSON, com a seguinte estrutura:

```json
{
  "author": {
    "name": "J.K. Rowling",
    "birth_date": "31 July 1965",
    "birth_place": "Yate, United Kingdom",
    "description": "Author of the Harry Potter series..."
  },
  "quotes": [
    {
      "text": "It is our choices that show what we truly are...",
      "tags": ["choices", "inspirational", "philosophy"]
    },
    {
      "text": "It does not do to dwell on dreams and forget to live...",
      "tags": ["dreams", "life", "philosophy"]
    }
  ]
}
```
