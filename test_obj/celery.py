# coding:utf-8
from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings
import os

# 获取当前文件夹名，即为该Django的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化Celery
app = Celery('tasksss', broker='redis://:qqcqqc@47.102.138.171:6379/3')

# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings')

# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


""" 
命令启动 同manage.py文件目录下： 
执行任务：celery -A test_obj worker --pool=solo -l info
发布任务：elery -A test_obj beat
发布和执行一起：  celery -B -A test_obj  worker  
指定队列启动：celery -A test_obj worker -n dj_two -Q dj_two --pool=solo -l info
flower 启动： flower worker -A test_obj --port=8004


supervisorctl 命令
supervisorctl restart test-django:*  重启
supervisorctl stop test-django:*  停止
supervisorctl start test-django:*  开启
"""
