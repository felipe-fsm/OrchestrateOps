FROM python:3.9-slim

# Instala o curl e outras dependências necessárias
RUN apt-get update && apt-get install -y curl sqlite3

# Define o diretório de trabalho
WORKDIR /app

# Copia os requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Expõe a porta da aplicação
EXPOSE 80

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
