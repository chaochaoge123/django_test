from django.core.cache import cache
from .data_settings import *

def create_user_cache(user_id, value):
    cache.set(user_id, value, timeout=USER_TIME_OUT)


def get_user_cache(user_id):
    data = cache.get(user_id)
    if not data:
        """查数据库"""
        pass
    return data


def delete_user_cache(user_id):
    cache.delete(user_id)

