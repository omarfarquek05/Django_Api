from pathlib import Path
from environs import Env
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
#from environs import Env

env = Env()
env.read_env()  # This will read the .env file

cloudinary.config(
    cloud_name=env.str('CLOUDINARY_CLOUD_NAME'),
    api_key=env.str('CLOUDINARY_API_KEY'),
    api_secret=env.str('CLOUDINARY_API_SECRET')
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY = 'django-insecure-53^wkq!(*2t^4*lz@wgv06__tw$vz$r!=2%f&^lub1=&@x%aua'
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.100', '*']

# Application definition
INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.filters",  # optional, if special filters are needed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Products',
    'rest_framework',
    'import_export',
    "corsheaders",
    'django_filters',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware', 
   
]

ROOT_URLCONF = 'Api_Plus.urls'

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

WSGI_APPLICATION = 'Api_Plus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(env.str('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL for serving static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (user-uploaded files)
MEDIA_URL = '/media/'  # URL for serving media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directory for storing media files

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_HEADER": "Django Administration ",
    }

# Allow CORS for all origins (use this cautiously in production)
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",  # or the URL of your Next.js app
# ]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10  # Specify the number of products per page
}



