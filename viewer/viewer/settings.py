import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("Не прочел секретеый ключ, либо его просто нет")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_plotly_dash.apps.DjangoPlotlyDashConfig",
    "channels",
    "django_loguru",
    "blogers",
    "logs.apps.LogsConfig",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

PLOTLY_COMPONENTS = [
    "dash_core_components",
    "dash_html_components",
    "dash_renderer",
    "dpd_components",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_plotly_dash.middleware.BaseMiddleware",
]

ASGI_APPLICATION = "viewer.routing.application"

WSGI_APPLICATION = "viewer.wsgi.application"


ROOT_URLCONF = "viewer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB_USERS"),
        "USER": os.environ.get("POSTGRES_USER_USERS"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD_USERS"),
        "HOST": os.environ.get("POSTGRES_HOST_USERS"),
        "PORT": "5432",
        "OPTIONS": {
            "client_encoding": "UTF8",
        },
    },
    "logs_db": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB_LOGS"),
        "USER": os.environ.get("POSTGRES_USER_LOGS"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD_LOGS"),
        "HOST": os.environ.get("POSTGRES_HOST_LOGS"),
        "PORT": "5432",
    },
}

DATABASE_ROUTERS = ["db_routers.LogsDBRouter"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# настройки моих логов
DJANGO_LOGGING_MIDDLEWARE = {
    "DEFAULT_FORMAT": True,
    "MESSAGE_FORMAT": "<b><green>{time}</green> <cyan>{message}</cyan></b>",
    "LOG_USER": False,
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
