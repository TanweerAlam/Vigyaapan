"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# importing environment variables
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l&v)2s*bb5+x^o+3q4)+s1#9+f^=zwmxe%1@llz_jv^o4yq=cf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'users',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # sitemap
    # 'django.contrib.sites',
    'django.contrib.sitemaps',

    # Local app
    'main',
    'jobs',
    'newsletters',

    # Third-party batteries
    'tinymce',
    'crispy_forms',
    "crispy_bootstrap5",
    "django_social_share"
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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

# For uploading newsletter content
MEDIA_URL = 'uploaded_newsletters/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CRISPY_TEMPLATE_PACK = 'uni_form'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Login & logout redirection
LOGIN_REDIRECT_URL = "users:dashboard"
LOGOUT_REDIRECT_URL = "main:index"

# 
AUTH_USER_MODEL = "users.CustomUser"

# # Email backend
# EMAIL_HOST = "localhost"
# EMAIL_PORT = 1025

# Using mailgun as Email backend
# EMAIL_HOST = env('SMTP_HOSTNAME')
# EMAIL_PORT = env('SMTP_PORT')
# EMAIL_HOST_USER = env('SMTP_USERNAME')
# EMAIL_HOST_PASSWORD = env('SMTP_PASSWORD')
# EMAIL_USE_TLS = True

# Using sendgrid for Newsletters app
FROM_EMAIL = "tannumystic@gmail.com"
SENDGRID_API_KEY = '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'

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = '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' # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


# Tinymce settings
TINYMCE_DEFAULT_CONFIG = {
    'height' : "480",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap preview anchor"
    "fullscreen insertdatetime media table paste code help wordcount",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
#     # "language": "en_us",  # To force a specific language instead of the Django current language.
    'theme': "silver",
}
# TINYMCE_COMPRESSOR = True

# Django-sendgrid-v5 settings
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# Toggle sandbox mode (when running in DEBUG mode)
SENDGRID_SANDBOX_MODE_IN_DEBUG=False
# echo to stdout or any other file-like object that is passed to the backend via the stream kwarg.
SENDGRID_ECHO_TO_STDOUT=True