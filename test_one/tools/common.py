#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:47
# @Author  : qqc
# @File    : data_settings.py
# @Software: PyCharm



import hashlib
import time
from test_one.tools import *

def make_password(data):
    hl = hashlib.md5()
    hl.update(data.encode(encoding='utf-8'))
    hl.update('加点料'.encode(encoding='utf-8'))
    return hl.hexdigest()


def create_token():
    hl = hashlib.md5()
    hl.update(str(time.time()).encode(encoding='utf-8'))
    hl.update('加点料'.encode(encoding='utf-8'))
    return hl.hexdigest()
