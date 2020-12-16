# -*- coding: utf-8 -*-

class ErrorCode(object):
    """
    Error code
    """
    SUCCESS = ('10000', u'成功')
    API_PARAMS_ERROR = ('70001', u'API参数缺失或错误')
    API_VERIFY_ERROR = ('70002', u'验证错误')
    API_QINGQIU_MAX_ERROR = ('70003', u'当日请求次数已到上限')
    API_GONG_PARAMS_ERROR = ('70004', u'公共参数不全')
    API_NOT_SIGN_ERROR = ('70005', u'未登录')
    API_SIGN_GUOQI_ERROR = ('70006', u'登录时间过期')
    API_TOKEN_ERROR = ('70007', u'token错误')
    API_CACHE_TOKEN_ERROR = ('70008', u'缓存token错误')
