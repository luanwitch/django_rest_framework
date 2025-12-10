# 1. Usar imagem Python (Estável)
FROM python:3.11-slim

# 2. Configurar diretório de trabalho inicial e variável de ambiente
WORKDIR /app
ENV PYTHONUNBUFFERED 1 # Garante que o output seja enviado para o log do Docker imediatamente

# 3. Instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt \
    # Instalar dependências de banco de dados (se for usar o psycopg2)
    && apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copiar todo o conteúdo do projeto
# O 'manage.py' e a pasta 'config' estarão diretamente em /app/
COPY . /app/

# 5. Configurar o WORKDIR final
# Esta linha é redundante, pois o WORKDIR /app já foi definido, mas é inofensiva.
# WORKDIR /app 

# 6. Expôr a porta
EXPOSE 8000

# 7. Comando Final: Usar apenas a última linha CMD, executando o Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]