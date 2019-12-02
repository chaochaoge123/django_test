# encoding: utf-8
# import djcelery
# djcelery.setup_loader()
# CELERY_IMPORTS=(
#     'test_one.tasks.task1',
# )
# #有些情况可以防止死锁
# CELERYD_FORCE_EXECV=True
# # 设置并发worker数量
# CELERYD_CONCURRENCY=4
# #允许重试
# CELERY_ACKS_LATE=True
# # 每个worker最多执行100个任务被销毁，可以防止内存泄漏
# CELERYD_MAX_TASKS_PER_CHILD=100
# # 超时时间
# CELERYD_TASK_TIME_LIMIT=12*30

from __future__ import absolute_import
from celery import Celery

cel = Celery('celery_demo',
             broker='redis://:qqcqqc@172.29.32.104:6379/5',
             backend='redis://:qqcqqc@172.29.32.104:6379/6',
             # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['tasks.tasks1',
                      # 'celery_task.tasks2'
                      ])

# 时区
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc = False