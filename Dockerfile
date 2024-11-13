# Usa a imagem base minimalista Python 3.9
FROM python:3.9-slim

# Instala dependências básicas (curl e sqlite3)
RUN apt-get update && apt-get install -y --no-install-recommends curl sqlite3 \
    && rm -rf /var/lib/apt/lists/*  # Limpa o cache para reduzir o tamanho da imagem

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos primeiro (melhora o cache do Docker)
COPY requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Expõe a porta da aplicação (correta para 8080)
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
