#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 10:53
# @Author  : qqc
# @File    : pro.py
# @Software: PyCharm



from .common import *

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