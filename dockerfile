# Usar imagem Python
FROM python:3.11-slim

# Configurar diretório de trabalho inicial
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo o conteúdo do projeto da raiz do host para a raiz do contêiner
# Isso garante que a pasta 'django_rest_framework' (e o manage.py) sejam copiados para /app/
COPY . /app/

# CORREÇÃO: Definir o diretório de trabalho para a pasta raiz do projeto Django.
# Isso permite que o Gunicorn importe 'config.wsgi' diretamente.
WORKDIR /app/django_rest_framework

# Expôr porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor Django, que agora pode usar o caminho simplificado
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]



