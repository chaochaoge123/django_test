import time
from celery import task

@task
def add(a,b):
    time.sleep(10)
    return "第二个任务%s"%(a+b)