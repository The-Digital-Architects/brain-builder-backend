"""
Django settings for django_react_proj project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import random
import urllib
import dj_database_url


def get_random_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(random.choice(chars) for i in range(50))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

# Redirect all HTTP traffic to HTTPS -> not sure if this is necessary
SECURE_SSL_REDIRECT = False  # I SET THIS TO FALSE TO TRY DEBUG A 301 ISSUE -> TODO

# Instruct browsers to use HTTPS for all future requests
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


if IS_HEROKU_APP:
    ALLOWED_HOSTS = [
        "brain-builder-development-b6afefb63981.herokuapp.com",
        "www.brain-builder-development-b6afefb63981.herokuapp.com",
        "brain-builder.app",
        "www.brain-builder.app",
        "brain-builder-laurens-3406ee2c9cdb.herokuapp.com",
        "www.brain-builder-laurens-3406ee2c9cdb.herokuapp.com",
        "brain-builder-f6e4dc8afc4d.herokuapp.com",
        "www.brain-builder-f6e4dc8afc4d.herokuapp.com",
    ]
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'backend',
    'webpack_loader',
    'channels',
#    'django_eventstream',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

redis_url = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379'))

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [f'redis://:{redis_url.password}@{redis_url.hostname}:{redis_url.port}'],
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'django_react_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'public')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_react_proj.wsgi.application'

ASGI_APPLICATION = "django_react_proj.asgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
#    'default': dj_database_url.config(default='postgres://aaoydsqplnytyj:34b115476ab35523b0e68c244b7dc27b7c115a96d7692d510c0bf0131f890a6b@ec2-34-242-154-118.eu-west-1.compute.amazonaws.com:5432/dan5645q1865tq', conn_max_age=0)
    'default': dj_database_url.config(
        default = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')), conn_max_age=0
    )
}

# Cache setup -> we're using redis-cloud for this as well
# Currently cache is only used in the backend to store the data and neural networks, so they don't have to be retrained every time
# Watch out though: removing this will mean the predict function can't access the networks anymore and will break.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{redis_url.hostname}:{redis_url.port}",
        "OPTIONS": {
            "PASSWORD": redis_url.password,
            "DB": 0,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/',
        'STATS_FILE': os.path.join(BASE_DIR, 'build', 'bundle-stats.json'),
    }
}

# Configure app for Heroku deployment
django_heroku.settings(locals())

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

# Place static in the same location as webpack build files
STATIC_ROOT = os.path.join(BASE_DIR, 'build')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build', 'static')]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
