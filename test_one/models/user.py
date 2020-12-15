# encoding: utf-8

from django.db import models
from test_one.tools.common import *

class User_info(models.Model):
    u"""用户信息"""
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')
    user_id = models.IntegerField(default=0, verbose_name=u'用户ID')
    name = models.CharField(default=u'', null=True, blank=True, max_length=100, verbose_name=u'名称')
    password= models.CharField(default=u'',null=True,blank=True, max_length=100, verbose_name="密码")
    mobile = models.CharField(default='', unique=True, max_length=15, null=True, blank=True, verbose_name=u'手机号')
    # mobile_authenticated = models.BooleanField(default=False, verbose_name=u'手机认证状态')
    remarks = models.CharField(default=u'', max_length=200, null=True, blank=True, verbose_name=u'简介')
    state = models.PositiveSmallIntegerField(default=0, verbose_name=u'记录状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    @classmethod
    def user_is_exist(cls, name):
        user_da = cls.objects.filter(name=name, state=0).first()
        if user_da:
            return True
        else:
            return False

    @classmethod
    def create_user(cls, name, mobile, password):
        cls.objects.create(name=name, mobile=mobile, password=hashlib_tool(password))

    class Meta:
        app_label = 'test_one'
        db_table = 'user_info'
        verbose_name = u'用户表'
        verbose_name_plural = u'用户表'



class Item(models.Model):
    case_no = models.CharField(default=u'', blank=False, max_length=32, verbose_name=u'方案编号')
    item_no = models.CharField(default=u'', blank=False, max_length=32, verbose_name=u'商品编号')


class IpInfo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')
    user_ip = models.CharField(default=u'', blank=False, max_length=32, verbose_name=u'IP地址')
    count = models.IntegerField(default=0, verbose_name=u'当天访问次数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        app_label = 'test_one'
        db_table = 'ip_info'
        verbose_name = u'访问信息'
        verbose_name_plural = u'访问信息'


class UserToken(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')
    user_id = models.IntegerField(default=0, verbose_name=u'用户ID')
    token = models.CharField(default=u'', max_length=256, blank=True, verbose_name=u'token')
    overdue_time = models.DateTimeField(auto_now_add=True, verbose_name=u'过期时间')
    state = models.PositiveSmallIntegerField(default=0, verbose_name=u'记录状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    @classmethod
    def create_or_update_token(cls, user_id, token, overdue_time):
        data = cls.objects.filter(user_id=user_id, state=0).first()
        if data:
            data.token = token
            data.overdue_time = overdue_time
            data.save()
        else:
            data = cls.objects.create(user_id=user_id, token=token, overdue_time=overdue_time)
        return data

    class Meta:
        app_label = 'test_one'
        db_table = 'user_token'
        verbose_name = u'用户token'
        verbose_name_plural = u'用户token'