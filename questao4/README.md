# Questão 4: Conexão com serviço FTP via conector Java

Nesta questão, foi realizado o download de um conector Java, seguido de sua execução para descobrir os dados de acesso (host, usuário e senha) necessários para conectar ao serviço FTP. Após a conexão, foi localizado um arquivo no servidor FTP e seu conteúdo foi extraído.

## Uso do Wireshark

Para capturar as credenciais de rede (host, usuário e senha) durante a comunicação com o servidor FTP, foi utilizado o **Wireshark**, uma ferramenta de análise de tráfego de rede. Através dele, foi possível monitorar o tráfego da conexão estabelecida pelo conector Java e obter as credenciais necessárias para acessar o servidor.

### Etapas:

1. **Download e execução do conector Java**:
   - O conector Java foi baixado e executado para iniciar a comunicação com o serviço FTP.

2. **Captura de tráfego com o Wireshark**:
   - O **Wireshark** foi utilizado para monitorar o tráfego de rede durante a execução do conector .jar
   - As credenciais de acesso (host, usuário, senha) foram extraídas diretamente do tráfego de rede capturado.

3. **Conexão ao servidor FTP**:
   - Com as credenciais obtidas, foi estabelecida a conexão ao servidor FTP utilizando um cliente FTP.

4. **Localização e extração do arquivo**:
   - O arquivo solicitado foi localizado dentro do FTP e seu conteúdo foi extraído.

5. **Criação do arquivo `Questao4.txt`**:
   - Um arquivo `Questao4.txt` foi criado contendo as seguintes informações:
     - Host
     - Usuário
     - Senha
     - Nome do arquivo encontrado
     - Conteúdo do arquivo

## Como o Wireshark foi utilizado

- O Wireshark capturou pacotes de rede gerados pelo conector Java durante a tentativa de conexão ao FTP.
- Ao analisar esses pacotes, foi possível identificar os dados de autenticação enviados em texto claro, permitindo a descoberta do host, usuário e senha para acessar o servidor FTP.

## Resultado

- O arquivo `Questao4.txt` contém:
  - **Host**: 52.200.142.116
  - **Usuário**: ctflteste
  - **Senha**: YdrTXPF#mcG7KUT#H@$P
  - **Nome do arquivo**: Great Job.txt
  - **Conteúdo do arquivo**: Your server is not safe, try for new password ideas in next time.ldoebaot.h
