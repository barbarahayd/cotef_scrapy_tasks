# imagem base do Python 
FROM python:3.9-slim

# instalar dependências para o Selenium, Firefox e outros
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    curl \
    gnupg \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libasound2 \
    xvfb \
    xauth \
    libnss3 \
    libxrender1 \
    libxtst6 \
    libx11-xcb1 \
    libdbus-1-3 \
    && rm -rf /var/lib/apt/lists/*

# baixar / instalar GeckoDriver (para o Firefox)
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.35.0-linux64.tar.gz \
    && chmod +x geckodriver \
    && mv geckodriver /usr/local/bin/

# instalar Selenium 
RUN pip install selenium

# diretório de trabalho dentro do container
WORKDIR /usr/src/app

# cria o diretório output dentro do container
RUN mkdir -p /usr/src/app/output

# copia o script Python do host para o container
COPY questao1-script.py /usr/src/app/

# executa o Firefox usando Xvfb para simular um ambiente gráfico
CMD ["sh", "-c", "Xvfb :99 -ac & export DISPLAY=:99 && python /usr/src/app/questao1-script.py"]

