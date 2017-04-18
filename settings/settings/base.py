# -*- coding: utf-8 -*-
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ROOT_URLCONF = 'settings.urls'
LANGUAGE_CODE = 'es-PA'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if str(DEBUG) == 'True':
    ALLOWED_HOSTS = ['*']
    WSGI_APPLICATION = 'settings.wsgi_base.application'
    SITE_URL = '/'
elif str(DEBUG) == 'False':
    ALLOWED_HOSTS = ['192.34.61.100','phx.dev2tech.xyz','phoenixworldtrade.com','www.phoenixworldtrade.com']
    WSGI_APPLICATION = 'settings.wsgi_prod.application'
    SITE_URL = 'http://www.phoenixworldtrade.com'

# DB CONF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# APPS CONF
LOCAL_APPS = [
    'local_apps.brands',
    'local_apps.blog',
    'local_apps.countries',
    'local_apps.dashboard',
    'local_apps.frontend',
    'local_apps.profiles',
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'ckeditor',
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# SECURITY CONF
LOGIN_URL = 'dashboard'
LOGIN_REDIRECT_URL = '/dashboard/'
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
    'local_apps.profiles.EmailBackend.EmailBackend',
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
                'settings.settings.custom_context_processors.menu',
                'settings.settings.custom_context_processors.lang',
            ],
        },
    },
]

# STATICFILES_DIRS = (
#     os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles')),
# )

STATIC_ROOT = os.path.abspath(
    os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'media'))


