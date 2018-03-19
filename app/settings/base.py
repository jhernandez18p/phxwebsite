# -*- coding: utf-8 -*-
import os
from decouple import config

# Site ID
SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
ROOT_URLCONF = 'app.urls.base'
LANGUAGE_CODE = 'es_PA'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if config('DEBUG', cast=bool) == True:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    WSGI_APPLICATION = 'app.wsgi_base.application'
    SITE_URL = '/'
else:
    DEBUG = False
    ALLOWED_HOSTS = ['test.phoenixworldtrade.com','phoenixworldtrade.com','www.phoenixworldtrade.com']
    WSGI_APPLICATION = 'app.wsgi_base.application'
    # WSGI_APPLICATION = 'app.wsgi_prod.application'
    SITE_URL = 'https://www.phoenixworldtrade.com'
# print(DEBUG)

# DB CONF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(os.path.join(BASE_DIR, 'dbs'), 'db.sqlite3'),
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'dbs'),
)

# APPS CONF
LOCAL_APPS = (
    'src.brands',
    'src.blog',
    'src.countries',
    'src.dashboard',
    'src.frontend',
    'src.multimedia',
    'src.profiles',
    'src.timeline',
)
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
)
THIRD_PARTY_APPS = (
    'rest_framework',
    'ckeditor',
)
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# SECURITY CONF
LOGIN_URL = 'dashboard'
LOGIN_REDIRECT_URL = '/dashboard'
LOGOUT_REDIRECT_URL = SITE_URL
SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_NAME = 'session'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'src.profiles.EmailBackend.EmailBackend',
]

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

# MEDIA CONF
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.abspath(
                os.path.join(
                    os.path.join(
                            BASE_DIR,os.pardir
                        ),
                        'templates')
                    ),
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.settings.custom_context_processors.menu',
                'app.settings.custom_context_processors.cookies',
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles')),
)

# STATIC_ROOT = os.path.abspath(
#     os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR,os.pardir), 'media')


# Django Rest Framework Setup
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

GOOGLE_MAPS_API_KEY = 'AIzaSyA_uf0M6P9N8ZUTm3vsKlm-li2auJ9-guU'
APPEND_SLASH = True