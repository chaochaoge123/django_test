
import redis
POOL = redis.ConnectionPool(host='172.29.32.104', port=6379,password='qqcqqc',max_connections=1000)


"""
linux-centos7 服务端启动：
redis-server /qqc_pack/redis-2.8.17/redis.conf

客户端：
redis-cli 
auth qqcqqc

"""