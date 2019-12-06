from django.core.management.base import BaseCommand
from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest
import json
import oss2
import os
from test_obj import settings
import logging
from itertools import islice

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_oss()

    @staticmethod
    def add_oss():
        # access_key_id = settings.ALIYUN_ACCESS_KEY_ID
        # access_key_secret = settings.ALIYUN_ACCESS_KEY_SECRET
        # bucket_name = settings.OSS_BUCKETS
        # endpoint = settings.OSS_ENDPOINT
        # sts_role_arn = settings.STS_ROLE
        #
        # clt = client.AcsClient(access_key_id, access_key_secret, bucket_name)
        # print(clt,"LLLLLLL")
        # req = AssumeRoleRequest.AssumeRoleRequest()
        #
        # req.set_accept_format('json')
        # req.set_RoleArn(sts_role_arn)
        # req.set_RoleSessionName('oss-python-sdk-example')
        # rsp = clt.do_action_with_exception(req)
        # print(rsp)
        # rsp_data = json.loads(rsp)
        # print(rsp_data)


        pass


