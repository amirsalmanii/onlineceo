from pathlib import Path
from . import secret

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secret.s_key

DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'accounts',
    'otp',
    'categories',
    'products',
    'threed',
    'discount',
    'mark',
    'order',
    'accounting',
    'news',
    'payments',
    'projects',
    # third party
    'rest_framework',
    'rest_framework.authtoken',
    'django_cleanup.apps.CleanupConfig',
    'django_crontab',
    'corsheaders',
    #'debug_toolbar', for dev mod
    'azbankgateways',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'config.urls'

CORS_ALLOW_ALL_ORIGINS = True

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': secret.db_eng,
        'NAME': secret.db_name,
        'USER': secret.db_user,
        'PASSWORD': secret.db_password,
        'HOST': secret.db_host,
        'PORT': secret.db_port,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

}

AUTH_USER_MODEL = 'accounts.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email settings
DEFAULT_FROM_EMAIL = secret.or_email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = secret.or_email
EMAIL_HOST_PASSWORD = secret.or_email_p
EMAIL_PORT = 587
EMAIL_USE_TLS = True 

CRONJOBS = [
    ('1 0 * * *', 'discount.cron.my_scheduled_job')
]

# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",   # for dev mood
#     # ...
# ]

#gateway config

AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'ZARINPAL': {
            'MERCHANT_CODE': secret.m_id_zarinpal,
        },
    },
    'IS_SAMPLE_FORM_ENABLE': True,
    'DEFAULT': 'BMI',
    'CURRENCY': 'IRR', 
    'TRACKING_CODE_QUERY_PARAM': 'tc', 
    'TRACKING_CODE_LENGTH': 16, 
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', 
    'BANK_PRIORITIES': [
        'ZARINPAL'
    ],
}
