import os
import os
from datetime import timedelta
from pathlib import Path
from pathlib import Path

from decouple import Csv
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-#^wi4zgf9o!grx0*6+xrcvri*rto102djufx^6y)=(uad%d5dx",
    cast=str,
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", default="", cast=Csv())
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="[*]", cast=Csv())
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_connect_backend",
    "django_connect_backend.templatetags",
    "django_connect_api",
    "rest_framework",
    "rest_framework.authtoken",
    'django_redis',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_connect_store.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "django_connect_store.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

REDIS_HOST = config("REDIS_HOST", default="127.0.0.1", cast=str)
REDIS_PORT = config("REDIS_PORT", default="6379", cast=str)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

MAIN_DATABASE_NAME = config("MAIN_DATABASE_NAME", default="maindb", cast=str)
MAIN_DATABASE_USER = config("MAIN_DATABASE_USER", default="maindb", cast=str)
MAIN_DATABASE_PASSWD = config("MAIN_DATABASE_PASSWD", default="secret", cast=str)
MAIN_DATABASE_HOST = config("MAIN_DATABASE_HOST", default="127.0.0.1", cast=str)
MAIN_DATABASE_PORT = config("MAIN_DATABASE_PORT", default="3306", cast=str)
MAIN_DATABASE_ENGINE = config(
    "MAIN_DATABASE_ENGINE", default="django.db.backends.sqlite3", cast=str
)
DATABASES = {
    "default": {
        "ENGINE": MAIN_DATABASE_ENGINE,
        "NAME": MAIN_DATABASE_NAME,
        "USER": MAIN_DATABASE_USER,
        "PASSWORD": MAIN_DATABASE_PASSWD,
        "HOST": MAIN_DATABASE_HOST,
        "PORT": MAIN_DATABASE_PORT,
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us", cast=str)

TIME_ZONE = config("TIME_ZONE", default="UTC", cast=str)

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "django_connect_backend/static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"