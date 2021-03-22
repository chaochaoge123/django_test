#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 10:53
# @Author  : qqc
# @File    : pro.py
# @Software: PyCharm



from .common import *

DEBUG = False

# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.102.138.171:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "qqcqqc",
        }
    }
}


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
CELERY_TIMEZONE = 'Asia/Shanghai'

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
    'test_one.tasks.add_six': {'queue': 'dj_two', 'routing_key': 'dj_two'},
    'test_one.tasks.add_four': {'queue': 'dj_two', 'routing_key': 'dj_two'}
}