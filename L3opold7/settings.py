# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0i9ew9l2n0bh%ks2y&_pa_u=*h&2v%m@ex3pxv)+jd-iud2&18'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'common',
    'imagekit',
    'pipeline',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'L3opold7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'L3opold7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# Django Pipeline

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'blog': {
            'source_filename': (
                'css/blog.css',
            ),
            'output_filename': 'css/blog.css'
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "common.UserProfile"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # AWS Setting
    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = 'l3opold7'
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
    AWS_ACCESS_KEY_ID = 'AKIAJA7YZMQQ5GG7LTPQ'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # Static Setting
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    #Media Setting
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
