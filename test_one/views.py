from django.shortcuts import render,HttpResponse
import time
import django.dispatch
from django.dispatch import receiver
from django.http import JsonResponse
from test_one.tools import create_user_cache,get_user_cache
from django_redis import get_redis_connection
from test_one.models.user import User_info,UserToken
from .import tasks
from test_one.tools.user_tool import *
from test_one.tools.common import *
from test_one.tools import redis_pool,cache_tool
import json

# 信号
work_done = django.dispatch.Signal(providing_args=['path', 'time'])

def create_signal(request):
    url_path = request.path
    print("我已经做完了工作。现在我发送一个信号出去，给那些指定的接收器。")

    # 发送信号，将请求的url地址和时间一并传递过去
    work_done.send(create_signal, path=url_path, time=time.strftime("%Y-%m-%d %H:%M:%S"))
    return HttpResponse("200,ok")

@receiver(work_done, sender=create_signal)
def my_callback(sender, **kwargs):
    print("我在%s时间收到来自%s的信号，请求url为%s" % (kwargs['time'], sender, kwargs["path"]))



def tem_test(request):
    return render(request, "search.html")


# redis连接
def resdis_test(request):
    conn = get_redis_connection('default')
    all=conn.get("age")
    print(all,"CCCCCCCCCCC")
    data={"age":all.decode()}
    print(type(data))
    return JsonResponse(data=data, safe=False)

import os
def tset_user_cz(request):
    user_id = request.GET["user_id"]
    print(request.META.get("DJANGO_SETTINGS_MODULE"),"DFFFFFFFFFFFFFFFFFFFFF")
    print(os.environ.get("DJANGO_SETTINGS_MODULE"),"SSSSSSSSSSSSSSSS")
    # User_info.objects.create(user_id=user_id, name="name", password="123456", remark="庐州", mobile="22222")

    info = get_user_cache(user_id)
    print(info,"DDDDDDDDDDDDDDDDDDDDDDDDDDD")
    if not info:
        values = User_info.objects.filter(id=user_id).values_list("password", "mobile")
        data = {"password": values[0][0], "mobile": values[0][1]}
        create_user_cache(user_id, data)
        return JsonResponse(data=data, safe=False)

    return JsonResponse(data=info, safe=False)


@user_ip_required
def celery_t(request):
    tasks.add.delay(1, 2)
    tasks.add_three.delay(50, 55)
    result = {'code': 0, 'msg': 'hello'}
    return JsonResponse(result)


def search_tool(request):
    return render(request, "search.html")



def sentry_test(request):
    age = int(request.GET.get('age'))
    print("最新版本测试，v0.2版本UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU:wq"
          "")
    return JsonResponse({'age': age})


def queue_test(request):
    res=tasks.add_four.delay(33, 44)
    print(res, "############################")

    tasks.add_six.delay(333, 444)
    result = {'code': 0, 'msg': 'add_four'}
    print("远程代码覆盖待本地的内容########################")
    return JsonResponse(result)


@user_ip_required
@user_login_required
def t_gevent(request):
    print(request.user_id,request.token,"DDDDDDDDDDDD")
    time.sleep(3)
    # user=User_info.objects.filter(id=1).first()
    # u=user.user_id
    # if u==1:
    #     user.user_id=u-1
    #     user.save()
    #     return JsonResponse({'user_id':user.user_id,'messsge':"减数成功"})
    return JsonResponse({'user_id':0,'messsge':"减数失败"})



def user_zc(request):
    name=request.GET.get("name")
    mobile = request.GET.get("mobile")
    password = request.GET.get("password")
    re_password = request.GET.get("re_password")
    if User_info.user_is_exist(name):
        return JsonResponse({'error_message': "用户名已存在", "status_code": 702})
    if password != re_password:
        return JsonResponse({'error_message': "密码不一致", "status_code": 703})
    User_info.create_user(name, mobile,password)
    return JsonResponse({'message': "创建成功", "status_code": 10000})


def user_dl(request):
    name = request.GET.get("name")
    password = request.GET.get("password")
    if not User_info.user_is_exist(name):
        return JsonResponse({'error_message': "用户名不存在", "status_code": 704})
    u_info = User_info.objects.filter(name=name, state=0).first()
    if u_info.password != make_password(password):
        return JsonResponse({'error_message': "密码错误", "status_code": 705})

    data = UserToken.create_or_update_token(u_info.id, create_token(),
                                       overdue_time=datetime.datetime.now() + datetime.timedelta(days=1))
    user_data = {
        'id': u_info.id,
        'name': u_info.name,
        'mobile': u_info.mobile,
        'token': data.token,
        'overdue_time': data.overdue_time.strftime('%Y-%m-%d %H:%M:%S'),
        'password': u_info.password
    }

    cache_tool.delete_user_cache('user_id_%s' % (u_info.id))
    cache_tool.create_user_cache('user_id_%s' % (u_info.id), json.dumps(user_data, ensure_ascii=False))
    return JsonResponse(user_data)
