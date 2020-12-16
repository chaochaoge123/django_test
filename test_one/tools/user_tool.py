#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 17:22
# @Author  : qqc
# @File    : ip_tool.py
# @Software: PyCharm

from django.utils.decorators import available_attrs
from functools import wraps
from test_one.models.user import User_info, IpInfo,UserToken
import datetime
from django.http import JsonResponse
from test_one.tools.cache_tool import *
from test_one.tools.error_code import *
from test_one.tools.response import *
import json


def user_ip_required(view_func):
    """
    """

    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get(
            'REMOTE_ADDR')

        ip_info = IpInfo.objects.filter(user_ip=ip, create_time__gte=datetime.datetime.now().date()).first()
        if ip_info:
            if ip_info.count >= 30:
                return APIResponse(error=ErrorCode.API_QINGQIU_MAX_ERROR)
            else:
                ip_info.count = ip_info.count + 1
                ip_info.save()
        else:
            IpInfo.objects.create(user_ip=ip, count=1)

        return view_func(request, *args, **kwargs)

    return wrapped_view


def user_login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        user_id = request.META.get("HTTP_USER_ID")
        token = request.META.get("HTTP_USER_TOKEN")
        if not user_id or not token:
            return APIResponse(error=ErrorCode.API_GONG_PARAMS_ERROR)
        cache_data = get_user_cache('user_id_%s' % (user_id))
        if not cache_data:
            t_da = UserToken.objects.filter(user_id=user_id, state=0).first()
            if not t_da:
                return APIResponse(error=ErrorCode.API_NOT_SIGN_ERROR)
            if datetime.datetime.now() > t_da.overdue_time:
                return APIResponse(error=ErrorCode.API_SIGN_GUOQI_ERROR)
            if token != t_da.token:
                return APIResponse(error=ErrorCode.API_TOKEN_ERROR)
        user_data = json.loads(cache_data)
        if token != user_data.get('token'):
            return APIResponse(error=ErrorCode.API_CACHE_TOKEN_ERROR)
        request.user_id, request.token = user_data.get('id'), user_data.get('token')

        return view_func(request, *args, **kwargs)

    return wrapped_view



def test():
    pass