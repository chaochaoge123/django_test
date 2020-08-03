import time
from celery import shared_task
from test_obj.celery import *


@app.task
def add(a, b):
    print("这是任务开始")
    print(a + b)
    time.sleep(10)
    print("这是任务结束")


@app.task
def add_two(a, b):
    print("第二个任务", a * b)
    time.sleep(5)
    print("结束")


@app.task
def add_three(a, b):
    print("第三个任务")
    time.sleep(5)
    print("第三个任务", a + b)

@app.task
def add_four(a,b):
    print("t_four---任务开始")
    time.sleep(3)
    print(a-b)
    print('t_four---任务结束')

@app.task
def add_five(a,b):
    print("t_five---任务开始")
    time.sleep(2)
    print('t_five---任务结束')


@app.task
def add_six(a, b):
    print("t_six---任务开始")
    time.sleep(2)
    print(a+b)
    print('t_six---任务结束')