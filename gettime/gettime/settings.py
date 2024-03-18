"""
Django settings for gettime project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import datetime
import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m4qhhbok=h+*96d++@j0r^+s2boxmacxk45_v7mt2s*c^ql)=$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gettime.urls'

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

WSGI_APPLICATION = 'gettime.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

def sendResponse(request, resultCode, data, action="no action"):
    response = {}
    response["resultCode"] = resultCode
    response["resultMassage"]= resultMessages[resultCode]
    response["data"] = data 
    response["size"] = len(data)
    response["action"] = action
    response["curdate"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return json.dumps(response, indent=4, sort_keys=True, default=str)

resultMessages = {
    
    200:"amjilttai",
    404: "oldsongui",
    1000:"burtgeh bolomjgui. mail hgayg umni ni burtgegdsen baina",
    1001:"hereglegch amjilttaiu burtgegdlee",
    1002:"batalgaajuulah mail ilgeelee",
    3002:"method error",
    3003:"json aldaa",
    3004:"action buruu",
    3005:"",
}
    
import psycopg2 as ps
import random, string

PGdbname="user"
PGuser="postgres"
PGpassword="1000"
PGport="5432"
PGhost="localhost"

def connectDB():
    con = ps.connect(
        # host = '192.168.0.15'
        dbname=PGdbname,
        user=PGuser,
        host=PGhost,
        password= PGpassword,
        port= PGport,
    )
    return con 
def disconnectDB(con):
    if(con):
        con.close()
def randomstr(lenght):
    character = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(character) for i in range(lenght))
    return password
            

