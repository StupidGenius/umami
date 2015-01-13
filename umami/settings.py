"""

The MIT License (MIT)

Copyright (c) 2011-2015 Mark Rogaski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.utils.crypto import get_random_string

import dj_database_url


# Build paths inside the project like this: os.path.join(ROOT_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Secret key is randomly generated if not set.
# For Heroku, use the following to set the configuration:
#
#     heroku config:set SECRET_KEY=`openssl rand -base64 32`
#     heroku config:set PYTHONHASHSEED=random
#
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_string(50,
    'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = bool(os.environ.get('TEMPLATE_DEBUG', False))
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '').split()

if DEBUG:
    SESSION_COOKIE_SECURE = False


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'registration',
    'widget_tweaks',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'sslify.middleware.SSLifyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'umami.urls'

WSGI_APPLICATION = 'umami.wsgi.application'


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        }
    }
}


# Database
DATABASES = { 
    'default': dj_database_url.config()
}


# Custom user model
AUTH_USER_MODEL = 'accounts.Member'


# Login accounts
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'


# E-mail transport
DEFAULT_FROM_EMAIL=os.environ.get('DEFAULT_FROM_EMAIL', '')
SERVER_EMAIL=os.environ.get('SERVER_EMAIL', '')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS', False))
EMAIL_USE_SSL = bool(os.environ.get('EMAIL_USE_SSL', False))


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)


