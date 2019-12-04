# encoding: utf-8

from django.db import models

class User_info(models.Model):
    u"""用户信息"""
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')
    user_id = models.IntegerField(default=0, unique=True, verbose_name=u'用户ID')
    name = models.CharField(default=u'', null=True, blank=True, max_length=100, verbose_name=u'名称')
    password= models.CharField(default=u'',null=True,blank=True, max_length=100, verbose_name="密码")
    mobile = models.CharField(default='', unique=True, max_length=15, null=True, blank=True, verbose_name=u'手机号')
    # mobile_authenticated = models.BooleanField(default=False, verbose_name=u'手机认证状态')
    remarks = models.CharField(default=u'', max_length=200, null=True, blank=True, verbose_name=u'简介')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        app_label = 'test_one'
        db_table = 'user_info'
        verbose_name = u'用户表'
        verbose_name_plural = u'用户表'



class Item(models.Model):
    case_no = models.CharField(default=u'', blank=False, max_length=32, verbose_name=u'方案编号')
    item_no = models.CharField(default=u'', blank=False, max_length=32, verbose_name=u'商品编号')