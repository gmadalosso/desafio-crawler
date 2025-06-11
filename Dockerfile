FROM python:3.10-slim

WORKDIR /app

#Instala dependências do Chrome e do Selenium
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    unzip \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/lib/chromium/:${PATH}"
ENV CHROME_BIN=/usr/bin/chromium

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p resultadosCSV resultadosJSON

CMD ["python", "app.py"]