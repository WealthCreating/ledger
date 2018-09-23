# ledger.settings.base
# Configurations that are common to all environments
#
# Author:  Benjamin Bengfort <benjamin@bengfort.com>
# Created: Sat Apr 14 10:24:26 2018 -0400
#
# ID: base.py [36d8a34] benjamin@bengfort.com $

"""
Django settings for ledger project that are common to all environments.

Originally generated by 'django-admin startproject' using Django 2.0.4 as
ledger.settings.py -- this file has been adapted to a multi-file settings
configuration.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os
import dj_database_url


##########################################################################
## Path and Helpers
##########################################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONFDIR = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(CONFDIR, "..", ".."))


def environ_setting(name, default=None):
    """
    Fetch setting from the environment or use default. If default is None then
    raise an ImproperlyConfigured exception.
    """
    if name not in os.environ and default is None:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(
            "The {0} ENVVAR is not set.".format(name)
        )

    return os.environ.get(name, default)


def parse_bool(val):
    if isinstance(val, str):
        if val.lower().startswith('f'):
            return False
        if val.lower().startswith('t'):
            return True

        val = int(val)
    return bool(val)


##########################################################################
## Secrets
##########################################################################

# WARNING: keep the secret key used in production secret!
SECRET_KEY = environ_setting("SECRET_KEY")


##########################################################################
## Database
##########################################################################

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600),
}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'


##########################################################################
## Runtime
##########################################################################

# WARNING: don't run with debug turned on in production!
DEBUG = parse_bool(environ_setting("DEBUG", True))

# Specify hosts in production settings
ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1']

# WSGI Configuration
ROOT_URLCONF = 'ledger.urls'
WSGI_APPLICATION = 'ledger.wsgi.application'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'social_django',
    'accounts',
    'taxes',
]

# Request handling
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True


##########################################################################
## Content (Static, Media, Templates)
##########################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    os.path.join(PROJECT, 'assets'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

##########################################################################
## Authentication
##########################################################################

LOGIN_URL = '/user/login/'
LOGIN_ERROR_URL = LOGIN_URL
LOGIN_REDIRECT_URL = '/'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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

# Support for Social Auth authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

##########################################################################
## Social Auth Settings
##########################################################################

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.debug.debug',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.debug.debug',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = environ_setting('GOOGLE_OAUTH2_CLIENT_ID', "")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = environ_setting('GOOGLE_OAUTH2_CLIENT_SECRET', "")
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['bengfort.com']
SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

# Exception handling
GOOGLE_OAUTH2_SOCIAL_AUTH_RAISE_EXCEPTIONS = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = True

##########################################################################
## Django REST Framework
##########################################################################

REST_FRAMEWORK = {
    ## API Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),

    ## Default permissions to access the API
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    ## Pagination in the API
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGINATE_BY': 50,
    'PAGINATE_BY_PARAM': 'per_page',
    'MAX_PAGINATE_BY': 200,
}

##########################################################################
## Logging and Error Reporting
##########################################################################

ADMINS = (
    ('Benjamin Bengfort', 'benjamin@bengfort.com'),
)

SERVER_EMAIL = 'Bengfort Server <server@bengfort.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = environ_setting("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = environ_setting("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[LEDGER] '
