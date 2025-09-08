# Usar imagem Python
FROM python:3.11-slim

# Configurar diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo o projeto
COPY . .

# Expôr porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
