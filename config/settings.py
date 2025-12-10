import os
from pathlib import Path
from decouple import config # Importando decouple
# -------------------- NOVO IMPORT --------------------
import dj_database_url # Para configurar o banco de dados do Heroku
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Carregando SECRET_KEY de uma variável de ambiente (ou usando um fallback)
# A função config() tenta ler a variável SECRET_KEY do ambiente
SECRET_KEY = config('SECRET_KEY', default='django-insecure-8bc##a)xkty$*7392eq-3tn%)ezwkn=gq!h#f#$f4j@kol%^tj')

# Carregando DEBUG de uma variável de ambiente (ou usando False por padrão)
# É CRUCIAL que o Heroku configure esta variável como False em produção
DEBUG = config('DEBUG', default=False, cast=bool) # Alterado default para False

ALLOWED_HOSTS = ['*'] # Permite o acesso do domínio do Heroku

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    # Adicione aqui outras apps como djangorestframework-simplejwt, etc. se estiverem faltando
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WHITENOISE: Adicionado corretamente para servir arquivos estáticos
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ... (TEMPLATES e WSGI_APPLICATION permanecem os mesmos) ...

WSGI_APPLICATION = 'config.wsgi.application'

# -------------------- CORREÇÃO DO BANCO DE DADOS PARA HEROKU --------------------
# O Heroku usa a variável DATABASE_URL. dj_database_url a converte para o Django.
DATABASES = {
    'default': dj_database_url.config(
        # Lendo DATABASE_URL do ambiente
        default=config('DATABASE_URL') 
    )
}
# --------------------------------------------------------------------------------


AUTH_PASSWORD_VALIDATORS = [
# ... (VALIDATORS permanecem os mesmos) ...
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# -------------------- CONFIGURAÇÃO STATIC FILES CORRIGIDA --------------------
STATIC_URL = 'static/'

# Diretório para coletar arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Whitenoise: Otimiza o serviço de arquivos estáticos em produção
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# -----------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}