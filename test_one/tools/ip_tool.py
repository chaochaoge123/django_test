#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 17:22
# @Author  : qqc
# @File    : ip_tool.py
# @Software: PyCharm

from django.utils.decorators import available_attrs
from functools import wraps
from test_one.models.user import User_info, IpInfo
import datetime
from django.http import JsonResponse


def user_ip_required(view_func):
    """
    """

    def wrapped_view(request, *args, **kwargs):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get(
            'REMOTE_ADDR')

        ip_info = IpInfo.objects.filter(user_ip=ip, create_time__gte=datetime.datetime.now().date()).first()
        if ip_info:
            if ip_info.count >= 10:
                return JsonResponse({'message': "当日请求次数已到上限", "status_code": 701})
            else:
                ip_info.count = ip_info.count + 1
                ip_info.save()
        else:
            IpInfo.objects.create(user_ip=ip, count=1)

        return view_func(request, *args, **kwargs)

    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
