import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '7*q@6%=eg=kgj+2(i=156egtt8t_99xbe7oyp=su7)x)80_uxg'

DEBUG = True

ALLOWED_HOSTS = ['*', ]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'rest_framework',
    'interface_test'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # url登录拦截中间件
    'interface_test.middleware.LoginCheckMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vote',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'CHARSET': 'utf8',
        'TIME_ZONE': 'Asia/Shanghai',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TOKEN_TIMEOUT = 3600
STATIC_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = (os.path.join(BASE_DIR, 'static').replace('\\', '/'))
STATIC_URL = '/static/'

# LOGGING = {
#     'version': 1,
#     # 是否禁用已经存在的日志器
#     'disable_existing_loggers': False,
#     # 日志格式化器
#     'formatters': {
#         'simple': {
#             'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
#             'datefmt': '%Y-%m-%d %H:%M:%S',
#         },
#         'verbose': {
#             'format': '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
#                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s',
#             'datefmt': '%Y-%m-%d %H:%M:%S',
#         }
#     },
#     # 日志过滤器
#     'filters': {
#         # 只有在Django配置文件中DEBUG值为True时才起作用
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # 日志处理器
#     'handlers': {
#         # 输出到控制台
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'formatter': 'simple',
#         },
#         # 输出到文件(每周切割一次)
#         'file1': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'access.log',
#             'when': 'W0',
#             'backupCount': 12,
#             'formatter': 'simple',
#             'level': 'INFO',
#         },
#         # 输出到文件(每天切割一次)
#         'file2': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'error.log',
#             'when': 'D',
#             'backupCount': 31,
#             'formatter': 'verbose',
#             'level': 'WARNING',
#         },
#     },
#     # 日志器记录器
#     'loggers': {
#         'django': {
#             # 需要使用的日志处理器
#             'handlers': ['file1', 'file2'],
#             # 是否向上传播日志信息
#             'propagate': True,
#             # 日志级别(不一定是最终的日志级别)
#             'level': 'DEBUG',
#         },
#     }
# }
