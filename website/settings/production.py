# from pathlib import Path
# import os

# # importing environment variables
# import environ
# env = environ.Env()
# environ.Env.read_env()

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# #


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# ALLOWED_HOSTS = ['testsarkari.pythonanywhere.com', 'www.sarkarivigyaapan.com', 'sarkarivigyaapan.com' ]

# Security
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 3600
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# SITE_ID = 1
# # Application definition

# INSTALLED_APPS = [
#     # 'users',

#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # sitemap
#     'django.contrib.sites',
#     'django.contrib.sitemaps',

#     # Local app
#     'main',
#     'jobs',
#     'newsletters',

#     # Third-party batteries
#     'tinymce',
#     # 'crispy_forms',
#     # "crispy_bootstrap5",
#     "django_social_share",
#     "taggit",
#     "taggit_autosuggest",
#     "admin_honeypot",
#     'django_cleanup.apps.CleanupConfig',
#     'maintenance_mode',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'maintenance_mode.middleware.MaintenanceModeMiddleware',
# ]

# ROOT_URLCONF = 'website.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [str(BASE_DIR.joinpath('templates'))],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'website.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }


# DATABASES = {
#     'default': {
#         'ENGINE': env('DATABASE_ENGINE'),
#         'NAME': env('DATABASE_USER')+'$'+env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD'),
#         'HOST': env('DATABASE_HOSTNAME'),
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Kolkata'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

# # For uploading newsletter content
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # Login & logout redirection
# # LOGIN_REDIRECT_URL = "users:dashboard"
# # LOGOUT_REDIRECT_URL = "main:index"

# #
# # AUTH_USER_MODEL = "users.CustomUser"

# # # Email backend
# # EMAIL_HOST = "localhost"
# # EMAIL_PORT = 1025

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # Using mailgun as Email backend
# EMAIL_HOST = env('SMTP_HOSTNAME')
# EMAIL_PORT = env('SMTP_PORT')
# EMAIL_HOST_USER = env('SMTP_USERNAME')
# EMAIL_HOST_PASSWORD = env('SMTP_PASSWORD')
# EMAIL_USE_TLS = env('SMTP_USE_TLS')

# # Using sendgrid for Newsletters app
# # FROM_EMAIL = "tannumystic@gmail.com"
# FROM_EMAIL = env('FROM_EMAIL')
# SENDGRID_API_KEY = env('SMTP_PASSWORD')

# # Django-sendgrid-v5 settings
# # EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# # Toggle sandbox mode (when running in DEBUG mode)
# SENDGRID_SANDBOX_MODE_IN_DEBUG=False
# # echo to stdout or any other file-like object that is passed to the backend via the stream kwarg.
# SENDGRID_ECHO_TO_STDOUT=True


# # Tinymce settings
# TINYMCE_DEFAULT_CONFIG = {
#     'height' : "480",
#     "menubar": "file edit view insert format tools table help",
#     "plugins": "advlist autolink lists link image charmap preview anchor"
#     "fullscreen insertdatetime media table paste code help wordcount",
#     "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
#     "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
#     "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
#     "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
#     "a11ycheck ltr rtl | showcomments addcomment code",
#     "custom_undo_redo_levels": 10,
# #     # "language": "en_us",  # To force a specific language instead of the Django current language.
#     'theme': "silver",
# }
# # TINYMCE_COMPRESSOR = True



# # Django-Taggit
# TAGGIT_CASE_INSENSITIVE = True

# from django.contrib.messages import constants as messages
# MESSAGE_TAGS = {
#         messages.DEBUG: 'alert-secondary',
#         messages.INFO: 'alert-info',
#         messages.SUCCESS: 'alert-success',
#         messages.WARNING: 'alert-warning',
#         messages.ERROR: 'alert-danger',
# }

# #
# #
# # Logging system
# # LOGGING = {
# #     'version': 1,
# #     'disable_existing_loggers': False,
# #     'formatters': {
# #         'verbose': {
# #             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
# #             'style': '{',
# #         },
# #         'simple': {
# #             'format': '{levelname} {message}',
# #             'style': '{',
# #         },
# #     },
# #     'filters': {
# #         'special': {
# #             '()': 'project.logging.SpecialFilter',
# #             'foo': 'bar',
# #         },
# #         'require_debug_true': {
# #             '()': 'django.utils.log.RequireDebugTrue',
# #         },
# #     },
# #     'handlers': {
# #         'console': {
# #             'level': 'INFO',
# #             'filters': ['require_debug_true'],
# #             'class': 'logging.StreamHandler',
# #             'formatter': 'simple'
# #         },
# #         'mail_admins': {
# #             'level': 'ERROR',
# #             'class': 'django.utils.log.AdminEmailHandler',
# #             'filters': ['special']
# #         }
# #     },
# #     'loggers': {
# #         'django': {
# #             'handlers': ['console'],
# #             'propagate': True,
# #         },
# #         'django.request': {
# #             'handlers': ['mail_admins'],
# #             'level': 'ERROR',
# #             'propagate': False,
# #         },
# #         'myproject.custom': {
# #             'handlers': ['console', 'mail_admins'],
# #             'level': 'INFO',
# #             'filters': ['special']
# #         }
# #     }
# # }


from .base import *

DEBUG = False

ALLOWED_HOSTS += ['testsarkari.pythonanywhere.com', 'www.sarkarivigyaapan.com', 'sarkarivigyaapan.com' ]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Using mailgun as Email backend
EMAIL_HOST = env('SMTP_HOSTNAME')
EMAIL_PORT = env('SMTP_PORT')
EMAIL_HOST_USER = env('SMTP_USERNAME')
EMAIL_HOST_PASSWORD = env('SMTP_PASSWORD')
EMAIL_USE_TLS = env('SMTP_USE_TLS')


# Database settings
DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_USER')+'$'+env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOSTNAME'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

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