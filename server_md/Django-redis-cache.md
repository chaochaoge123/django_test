### 1. redis安装配置
```
(1)到redis目录
[root@localhost redis-2.8.17]# ls
00-RELEASENOTES  CONTRIBUTING  deps     Makefile   README      runtest           sentinel.conf  tests
BUGS             COPYING       INSTALL  MANIFESTO  redis.conf  runtest-sentinel  src            utils

(2) redis 源码包安装 
	make

(3)修改环境变量
vim /etc/profile

添加以下一行:
export PATH=/qqc_pack/redis-2.8.17/src:$PATH

(4)生效配置
source /etc/profile

(5)启动服务端：redis-server &
客户端：redis-cli
指定配置启动：
redis-server /qqc_pack/redis-2.8.17/redis.conf

(6)查看进程：
[root@localhost ~]# ps -aux|grep redis
root     21692  0.1  0.4 140812  7876 ?        Sl   18:29   0:30 redis-server 0.0.0.0:6379
root     21869  0.0  0.2  20200  5192 pts/1    S+   18:48   0:00 redis-cli
root     22139  0.0  0.0 112724   992 pts/0    R+   23:34   0:00 grep --color=auto redis
(7) 修改密码，开放host
[root@localhost redis-2.8.17]# vi redis.conf
bind 0.0.0.0
# bind 127.0.0.1
# requirepass foobared
requirepass qqcqqc
(8) 登录
127.0.0.1:6379> auth qqcqqc
OK

```
### 2.django中配置,连接redis服务
```
1、setting中配置：
# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://172.29.32.104:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "qqcqqc",
        }
    }
}

2、views中使用：
from django_redis import get_redis_connection
def resdis_test(request):
    conn = get_redis_connection('default')
    all=conn.get("age")
    data={"age":all}
    print(type(data))
    return JsonResponse(data=data, safe=False)
    
3、cache命令操作：
到manage.py目录
[root@localhost test_pro]# python3 manage.py shell
Python 3.6.4 (default, Nov 25 2019, 21:07:27) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.cache import cache
>>> cache.get("name")
>>> cache.get("103")
{'password': '123456', 'mobile': '22222'}

4、在redis 中查看
127.0.0.1:6379> keys *
1) "name"
2) ":1:103"
3) "age"
127.0.0.1:6379> get ":1:103"
"\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\bpassword\x94\x8c\x06123456\x94\x8c\x06mobile\x94\x8c\x0522222\x94u."

5.业务场景中使用
def tset_user_cz(request):
    user_id = request.GET["user_id"]
    # User_info.objects.create(user_id=user_id, name="name", password="123456", remark="庐州", mobile="22222")

    info = get_user_cache(user_id)
    if not info:
        values = User_info.objects.filter(user_id=user_id).values_list("password", "mobile")
        data = {"password": values[0][0], "mobile": values[0][1]}
        create_user_cache(user_id, data)
        return JsonResponse(data=data, safe=False)

    return JsonResponse(data=info, safe=False)
    
6.缓存方法
from django.core.cache import cache

def create_user_cache(user_id, value):
    cache.set(user_id, value, timeout=300) # 默认过期时间5分钟

def get_user_cache(user_id):
    data = cache.get(user_id)
    if not data:
        """查数据库"""
        pass
    return data

def delete_user_cache(user_id):
    cache.delete(user_id)

```