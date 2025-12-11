# 1. Base Stage: Configura o ambiente Python
FROM python:3.12.1-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Instalação de dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Diretório da app
WORKDIR /app

# Copia requirements.txt
COPY requirements.txt .

# Instala dependências
RUN pip install -r requirements.txt

# Copia todo o projeto
COPY . .

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
