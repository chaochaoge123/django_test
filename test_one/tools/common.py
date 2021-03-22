#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:47
# @Author  : qqc
# @File    : data_settings.py
# @Software: PyCharm



import hashlib
import time
from test_one.tools import *
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64
import xlrd
import requests
from openpyxl import Workbook



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


def create_public_private_data():
    """ 生成公钥-私钥文件 """
    # 获取一个伪随机数生成器
    random_generator = Random.new().read
    # 获取一个rsa算法对应的密钥对生成器实例
    rsa = RSA.generate(1024, random_generator)

    # 生成私钥并保存
    private_pem = rsa.exportKey()
    with open('/tmp/rsa.key', 'wb') as f:
        f.write(private_pem)

    # 生成公钥并保存
    public_pem = rsa.publickey().exportKey()
    with open('/tmp/rsa.pub', 'wb') as f:
        f.write(public_pem)


def pub_key_encrypt(data, fpath=None):
    """
    公钥加密
    :param data: 数据源
    :param path: 公钥文件路径
    :return: 加密后的base64字符串
    """
    if not fpath:
        fpath = '/tmp/rsa.pub'
    with open(fpath, 'r') as f:
        public_key = f.read()
        rsa_key_obj = RSA.importKey(public_key)
        cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
        cipher_text = base64.b64encode(cipher_obj.encrypt(data.encode('utf-8')))
        return cipher_text


def pri_key_decrypt(cipher_text, fpath=None):
    """
    私钥解密
    :param cipher_text: 公钥加密的base64字符串
    :param fpath: 私钥文件路径
    :return: 解密的数据源
    """
    if not fpath:
        fpath = '/tmp/rsa.key'
    with open(fpath, 'r') as f:
        private_key = f.read()
        rsa_key_obj = RSA.importKey(private_key)
        cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
        random_generator = Random.new().read
        data = cipher_obj.decrypt(base64.b64decode(cipher_text.encode('utf-8')), random_generator)
        return data.decode('utf-8')
    # https://blog.csdn.net/weixin_33774308/article/details/91449248


def read_execl_data(fpath=None, sheet=None):
    """
    获取表格数据
    :param fpath: execl 表格路径
    :param sheet: 工作区
    :return: 字典格式数据
    """
    if not fpath or not sheet:
        return None

    wb = xlrd.open_workbook(fpath)

    sh = wb.sheet_by_name(sheet)
    sh = wb.sheets()[0]
    data_all = []
    print(sh.nrows, "###############")
    for i in range(1, sh.nrows):
        data_all.append(dict(zip(sh.row_values(0), sh.row_values(i))))
    return data_all


def create_execl_data(fpath=None, sheet_name=None, columns=None, datas=None):
    """
    生成execl文件
    :param fpath: 保存目录
    :param sheet_name: 工作区标题
    :param columns: 列名
    :param datas: 数据
    :return:
    """
    if not fpath or not columns or not datas:
        return None
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name if sheet_name else "默认sheet"
    sheet.append(columns)
    for data in datas:
        sheet.append(data)

    workbook.save(fpath)


def download_fpath(url=None, fpath=None, name=None):
    """
    下载文件
    :param url: 下载地址
    :param fpath: 存放路径
    :param name: 文件名
    :return:
    """
    if not url or not fpath or not name:
        return None

    res = requests.get(url, stream=True)
    with open(fpath + name, "wb") as f:
        f.write(res.content)
