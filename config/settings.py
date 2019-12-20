import os


###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = os.path.basename(BASE_DIR)


#####################
# Security settings #
#####################

SECRET_KEY = '<fake-secret-key>'

DEBUG = True

ALLOWED_HOSTS = ['*']


#################
# Core settings #
#################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


############
# Database #
############


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'merge_sample',
        'HOST': 'ik1-304-12171.vs.sakura.ne.jp',
        'USER': 'root',
        'PASSWORD': 'MineSqlPasswordLost',
    }
}

#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


############
# Messages #
############

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                      '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}


################
# Static files #
################

#以下２行はdjangoでcssやjsなどのファイルを入れておくところ
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

#STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


##################
# Authentication #
##################

AUTH_USER_MODEL = 'accounts.CustomUser'

#Midnight eye Goku
LOGIN_URL = 'home'
#ログイン後メイン画面に推移する
LOGIN_REDIRECT_URL = 'layworth'
LOGOUT_REDIRECT_URL = '/accounts/login/'


##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'iudicium1234@gmail.com'
EMAIL_HOST_PASSWORD = 'iudicium5678'
EMAIL_USE_TLS = True
