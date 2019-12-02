
import time
from celery import task

@task
def add(a,b):
    time.sleep(10)
    return "第一个任务%s"%(a+b)
