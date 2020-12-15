import redis
from .data_settings import *


def conn_redis():
    pool = redis.ConnectionPool(host='47.102.138.171', port=6379, password='qqcqqc')
    r_client = redis.Redis(connection_pool=pool)
    return r_client


def get(key):
    data = conn_redis().get(key)
    return data.decode() if data else ''


def set(key, value):
    conn_redis().set(key, value, ex=USER_TIME_OUT)


def delete(key):
    conn_redis().delete(key)

"""
linux-centos7 服务端启动：
redis-server /qqc_pack/redis-2.8.17/redis.conf

客户端：
redis-cli 
auth qqcqqc

"""