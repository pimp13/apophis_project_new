from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # Local apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # My apps
    "account.apps.AccountConfig",
    "base.apps.BaseConfig",
    "content.apps.ContentConfig",
    "aboutus.apps.AboutusConfig",
    "setting.apps.SettingConfig",
    "course.apps.CourseConfig",
    "website.apps.WebsiteConfig",
    # Install apps
    'ckeditor',
    'ckeditor_uploader',
    'django_render_partial',
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

ROOT_URLCONF = 'apophis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'apophis.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': BASE_DIR / config('DB_NAME'),
        # 'USER': config('DB_USER'),
        # 'PASSWORD': config('DB_PASSWORD'),
        # 'HOST': config('DB_HOST'),
        # 'PORT': config('DB_PORT'),
        # 'OPTIONS': {
        #     'charset': 'utf8mb4',
        #     'ssl': {'ca': None}
        # },
    }
}

# Password validation
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
LANGUAGE_CODE = config('LANG')

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Customize User model for dj
AUTH_USER_MODEL = 'account.User'

# CKEditor configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
# CKEDITOR_BUNDLES = {
#     'ckeditor': {
#         'base_path': '/path/to/ckeditor/',  # مسیر جدید CKEditor LTS
#         'version': '4.24.0',
#     },
# }
# customColorPalette = [
#     {
#         'color': 'hsl(4, 90%, 58%)',
#         'label': 'Red'
#     },
#     {
#         'color': 'hsl(340, 82%, 52%)',
#         'label': 'Pink'
#     },
#     {
#         'color': 'hsl(291, 64%, 42%)',
#         'label': 'Purple'
#     },
#     {
#         'color': 'hsl(262, 52%, 47%)',
#         'label': 'Deep Purple'
#     },
#     {
#         'color': 'hsl(231, 48%, 48%)',
#         'label': 'Indigo'
#     },
#     {
#         'color': 'hsl(207, 90%, 54%)',
#         'label': 'Blue'
#     },
# ]

# Meta Tags
META_SITE_PROTOCOL = 'https'
META_SITE_DOMAIN = 'www.yoursite.com'
META_SITE_NAME = 'آپوفیس Apophis'
META_USE_TITLE_TAG = 'آکادمی آموزشی آپوفیس برنامه نویسی و طراحی وبسایت و اپلیکیشن و هوش مصنوعی'