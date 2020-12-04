# encoding: utf-8
"""
Django settings for test_obj project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ak9d25s)=yce=z3+0ae1e^^2jgi72p6d1%9!6esacbpjzgcj$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_one.apps.TestOneConfig',
    'raven.contrib.django.raven_compat',
    # 'djcelery',
]

# celery worker backend 配置
# from tasksss import celery
#
# BROKER_BACKEND='redis'
# BOOKER_URL='redis://:qqcqqc@172.29.32.104:6379/5'
# CELERY_RESULT_BACKEND='redis://:qqcqqc@172.29.32.104:6379/6'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_obj.urls'

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

WSGI_APPLICATION = 'test_obj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'qqc',
        "PASSWORD": '123456',
        'NAME': 'test'
    }

}

# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "qqcqqc",
        }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# sentry 配置
RAVEN_CONFIG = {
    'dsn': 'https://e850247051e04a9aa83ce943e2476b83@o428107.ingest.sentry.io/5373101',
}

# 阿里云配置 oss 子用户
# ALIYUN_ACCESS_KEY_ID = "LTAI4GBcrapVModkeNaoRW"
# ALIYUN_ACCESS_KEY_SECRET = "cJIRJDVQSU2GFlAYGd2oP43hgJ61"
# OSS_BUCKETS = "qqc-one"
# OSS_ENDPOINT = "http://oss-cn-shanghai.aliyuncs.com"
# STS_ROLE = "acs:ram::1511164971246235:role/two"


from celery import platforms
from celery.schedules import crontab
# celery
BROKER_URL = 'redis://:qqcqqc@47.102.138.171:6379/3'
# celery结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = 'redis://:qqcqqc@47.102.138.171:6379/4'

# celery内容等消息的格式设置
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# celery时区设置，使用settings中TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE

platforms.C_FORCE_ROOT = True


# 定时任务
CELERYBEAT_SCHEDULE = {
    'schedule-test': {
        'task': 'test_one.tasks.add_two',
        'schedule': 200,
        'args': (4, 5)
    },

}

# celery 队列
from kombu import Exchange, Queue
CELERY_QUEUES = [
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('dj_one', Exchange('dj_one'), routing_key='dj_one'),
    Queue('dj_two', Exchange('dj_two'), routing_key='dj_two'),
]


CELERY_ROUTES = {
    'test_one.tasks.add_two': {'queue': 'default', 'routing_key': 'default'},
    'test_one.tasks.add_three': {'queue': 'dj_one', 'routing_key': 'dj_one'},
    'test_one.tasks.add_six': {'queue': 'dj_one', 'routing_key': 'dj_one'},
    'test_one.tasks.add_four': {'queue': 'dj_two', 'routing_key': 'dj_two'}
}