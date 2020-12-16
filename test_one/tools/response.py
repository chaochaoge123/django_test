#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:35
# @Author  : qqc
# @File    : response.py
# @Software: PyCharm



import json

from django.http import HttpResponse, JsonResponse

from test_one.tools import *


class APIResponse(HttpResponse):

    def __init__(self, data=None, error=None, *args, **kwargs):

        rsp = {}
        if error is not None:
            rsp.update({'code': error[0], 'msg': error[1]})
        else:
            success_data = ErrorCode.SUCCESS
            rsp.update({'code': success_data[0], 'msg': success_data[1], 'data': {}})

        if data is not None:
            rsp['data'] = data

        super(APIResponse, self).__init__(json.dumps(rsp), content_type='application/json', *args, **kwargs)


class JsonTestResponse(JsonResponse):

    def __init__(self, data=None, error=None, *args, **kwargs):

        rsp = {}
        if error is not None:
            rsp.update({'code': error[0], 'msg': error[1]})
        else:
            success_data = ErrorCode.SUCCESS
            rsp.update({'code': success_data[0], 'msg': success_data[1], 'data': {}})

        if data is not None:
            rsp['data'] = data

        super(JsonTestResponse, self).__init__(rsp, *args, **kwargs)