import time
from celery import shared_task

@shared_task
def add(a,b):
    print("这是任务开始")
    print(a+b)
    time.sleep(10)
    print("这是任务结束")


@shared_task
def add_two(a,b):
    print("第二个任务")
    time.sleep(5)
    print("结束")