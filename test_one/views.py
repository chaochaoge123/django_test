from django.shortcuts import render,HttpResponse
import time
import django.dispatch
from django.dispatch import receiver
from django.http import JsonResponse
from test_one.tools import create_user_cache,get_user_cache
from django_redis import get_redis_connection
from test_one.models.user import User_info
from .import tasks

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


def celery_t(request):
    tasks.add.delay(1, 2)
    tasks.add_three.delay(50, 55)
    result = {'code': 0, 'msg': 'hello'}
    return JsonResponse(result)


def search_tool(request):
    return render(request, "search.html")



def sentry_test(request):
    age = int(request.GET.get('age'))
    return JsonResponse({'age': age})


def queue_test(request):
    res=tasks.add_four.delay(33, 44)
    print(res, "############################")

    tasks.add_six.delay(333, 444)
    result = {'code': 0, 'msg': 'add_four'}
    return JsonResponse(result)


def t_gevent(request):
    user=User_info.objects.filter(id=1).first()
    u=user.user_id
    if u==1:
        user.user_id=u-1
        user.save()
        return JsonResponse({'user_id':user.user_id,'messsge':"减数成功"})
    return JsonResponse({'user_id':user.user_id,'messsge':"减数失败"})










