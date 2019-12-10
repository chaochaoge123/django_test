import time
from celery import shared_task

@shared_task
def add(a,b):
    time.sleep(10)
    return "第二个任务%s"%(a+b)