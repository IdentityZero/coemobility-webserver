"""
Django settings for parking_website project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-az!u=wrd1&ulls7#s613_%5m(0@3(*!7gp4k%g*v%uj(8r_wja"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['122.248.192.233']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 'corsheaders',

    "core",
    "Users",
    "Vehicles",
    "storages",
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

ROOT_URLCONF = "parking_website.urls"

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

WSGI_APPLICATION = "parking_website.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "myParking",
#         "USER" : "root",
#         "PASSWORD": "o/g6C_TNT9GacVv?1=l/r`N8-6*1S8",
#         "HOST": "localhost",
#         "PORT": 3306,
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "myParking",
        "USER" : "admin",
        "PASSWORD": "DAjCjeCsjckolfJcbkY2",
        "HOST": "coemobilitydb.cpks4sm0udv9.ap-southeast-1.rds.amazonaws.com",
        "PORT": 3306,
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
# CORS_ORIGIN_ALLOW_ALL = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = 'Users.AuthUser'

AWS_ACCESS_KEY_ID = 'AKIAU6GD3HR2UEA36WHG'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'coemobility'
AWS_STORAGE_BUCKET_NAME_THUMBNAILS = 'coemobility-thumbnails'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'ap-southeast-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

THUMBNAIL_BUCKET_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME_THUMBNAILS

DATA_SERVER_URL = 'http://122.248.192.233'
# DATA_SERVER_URL = 'http://localhost:8000'

DEFAULT_PROFILE_IMAGE = "profile_pics/profile.png"
DEFAULT_VEHICLE_IMAGE = "vehicle_pics/vehicle.png"

