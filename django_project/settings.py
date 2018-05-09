"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'O5sAnoJJY83aXBWhZIEQLit4nLALsGzyUPRP5nT1T4qteD0797'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

USE_I18N = True




# Application definition

INSTALLED_APPS = (
    'outdoor',
    'womens',
    'mens',
    'access',
    'pet',
    'django_contactme',
    'special',
    'head',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "pet.context_processors.woof",
                "access.context_processors.item",
                "mens.context_processors.most",
                "womens.context_processors.wost",
                "outdoor.context_processors.post",
                "special.context_processors.enter",
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Indiana/Indianapolis'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Live static configuration




MEDIA_ROOT = '/home/django/django_project/django_project/media'
MEDIA_URL = '/media/'


STATIC_ROOT = '/home/django/django_project/django_project/static'
STATIC_URL = '/static/'


EMAIL_HOST          = "smtp.gmail.com"
EMAIL_PORT          = "587"
EMAIL_HOST_USER     = "jgmyspotz@gmail.com"
EMAIL_HOST_PASSWORD = "beaner12"
EMAIL_USE_TLS       = True # Yes for Gmail
DEFAULT_FROM_EMAIL = "Joe Grounds <jgmyspotz@gmail.com>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Fill in actual EMAIL settings above, and comment out the
# following line to let this django demo sending emails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CONTACTME_SALT = b"es-war-einmal-una-bella-princesa-in-a-beautiful-castle"
CONTACTME_NOTIFY_TO = "Joe Grounds <jgmyspotz@gmail.com>"

