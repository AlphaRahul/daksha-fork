"""
Daksha
Copyright (C) 2021 myKaarma.
opensource@mykaarma.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
"""
Django settings for daksha project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'gj%7t91&c$*q&+fkx-wuug^i$0b@@lk26vd4txdq=)%_319hyy')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  '127.0.0.1'
]
CUSTOM_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(sep=',')
ALLOWED_HOSTS.extend(CUSTOM_ALLOWED_HOSTS)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'daksha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'daksha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

# Set Email to receive test reports
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
POSTMARK_TOKEN = os.environ.get('POSTMARK_TOKEN', '')

# Logs/reports configurations
LOG_FILE = os.environ.get('LOG_FILE', 'logs/uiengine.log')
STORAGE_PATH = os.environ.get('STORAGE_PATH', 'reports')
APACHE_URL = os.environ.get('APACHE_URL', '')

# Github Configurations (if you choose to store test ymls in github)

"""
If either GIT_USER OR GIT_PASSWORD OR both are empty then only Public Repository or Organisation can be accessed
If both GIT_USER and GIT_PASSWORD are given then Public/Private Repository or Organisation can be accessed
Please provide only one field either REPO_ORG or REPO_USER
If you want to use private repo of an Organisation then provide REPO_ORG
If you want to use public repo of individual then provide REPO_USER
"""
GIT_USER = os.environ.get('GIT_USER', '')
GIT_PASS = os.environ.get('GIT_PASS', '')
REPO_NAME = os.environ.get('REPO_NAME', '')
BRANCH_NAME = os.environ.get('BRANCH_NAME', '')
REPO_ORG = os.environ.get('REPO_ORG', '')
REPO_USER = os.environ.get('REPO_USER', '')


