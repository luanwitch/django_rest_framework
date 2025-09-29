import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url
from django.conf import settings


# ---------------------------
# BASE DIRECTORY
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECRET KEY e DEBUG
# ---------------------------
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-f*k@=53bc5!shef1-6w+m$-g)kspbaljz%8k4(j7iuc-u2_dyd"
)

DEBUG = config("DEBUG", default=False, cast=bool)

# ---------------------------
# ALLOWED HOSTS
# ---------------------------
ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS",
    default="127.0.0.1,localhost",
    cast=Csv()
)

# ---------------------------
# INSTALLED APPS
# ---------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #"django_extensions",
    "debug_toolbar",
    "rest_framework.authtoken",

    # apps do seu projeto
    'rest_framework',
    "api",
]

# ---------------------------
# TEMPLATES
# ---------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # opcional, se não tiver templates, pode deixar vazio: []
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ---------------------------
# MIDDLEWARE
# ---------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Para servir estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# ---------------------------
# URLS e WSGI
# ---------------------------
ROOT_URLCONF = "config.urls"  
WSGI_APPLICATION = "config.wsgi.application"  

# ---------------------------
# DATABASE (PostgreSQL / fallback SQLite)
# ---------------------------
# Heroku fornece a DATABASE_URL automaticamente quando você adiciona o add-on Heroku Postgres.
# dj_database_url.config() interpreta essa URL e transforma em dicionário de configuração do Django.
# conn_max_age ajuda na persistência de conexões; ssl_require=True força SSL no Heroku.
DATABASES = {
    "default": dj_database_url.config(
        default=config(
            "DATABASE_URL",
            default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",  # fallback local
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

# ---------------------------
# PASSWORD VALIDATION
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------
# INTERNATIONALIZATION
# ---------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------------
# STATIC FILES
# ---------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------------------
# REST FRAMEWORK
# ---------------------------
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# ---------------------------
# INTERNAL IPS (Debug Toolbar)
# ---------------------------
INTERNAL_IPS = [
    "127.0.0.1",
]

# ---------------------------
# Configs de produção Heroku
# ---------------------------
# Forçar HTTPS no Heroku
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
