import oss2
from django.core.management.base import BaseCommand
from itertools import islice
import logging
from itertools import islice
class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_oss()

    @staticmethod
    def add_oss():

        # auth=oss2 .Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        # bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'qqc-data')
        # 设置存储空间为私有读写权限。
        # bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)

        # 上传文件
        # res=bucket.put_object_from_file('requirements.txt', r'E:\news\test_obj\requirements.txt')
        # print(res,"##############")

        # 下载文件
        # res=bucket.get_object_to_file('data_img/ac6eddc451da81cbc77979445e66d01608243198.jpg', r'E:\news\test_obj\gg.jpg')
        # print(res)

        # 遍历远程bucket文件
        # for b in islice(oss2.ObjectIterator(bucket), 10):
        #     print(b.key)

        # 删除文件
        # res=bucket .delete_object('requirements.txt')
        # print(res)

        # oss域名初始化
        # auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        # endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
        # bucket = oss2.Bucket(auth, endpoint, 'qqc-data')
        # print(res)

        # 自定义域名初始化
        # cname = 'https://www.qqc-home.com/'
        # bucket = oss2.Bucket(auth, cname, 'qqc-data', is_cname=True)

        # 创建储存空间(qqc-one)
        # auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        # bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'qqc-one')
        # bucketConfig = oss2.models.BucketCreateConfig(oss2.BUCKET_STORAGE_CLASS_STANDARD,
        #                                               oss2.BUCKET_DATA_REDUNDANCY_TYPE_ZRS)
        # bucket.create_bucket(oss2.BUCKET_ACL_PRIVATE, bucketConfig)
        # bucket.create_bucket()

        # 列举储存空间
        auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        service = oss2.Service(auth, 'http://oss-cn-shanghai.aliyuncs.com')
        print([b.name for b in oss2.BucketIterator(service)])

        # 查看bucket信息
        # auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        # bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'qqc-data')
        # res=bucket.get_bucket_info()
        # print(res.name)

        #判断文件是否存在
        # auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        # bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'qqc-data')
        # exist = bucket.object_exists('data_img/ac6eddc451da81cbc77979445e66d01608243198.jpg')
        # print(exist)
        # 文件权限
        # print(bucket.get_object_acl('data_img/ac6eddc451da81cbc77979445e66d01608243198.jpg').acl)
        # 获取文件元信息
        # res=bucket.head_object('data_img/ac6eddc451da81cbc77979445e66d01608243198.jpg')
        # print(res.headers)

        # 日志
        log_file_path = r"E:\news\test_obj\log.log"
        # 开启日志
        oss2.set_file_logger(log_file_path, 'oss2', logging.INFO)
        auth = oss2.Auth('LTAI4tPApE68Wui2', 'oLPVMEO7ShOEH0fqVche9fT6b90MlQ')
        bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'qqc-data')

        for b in islice(oss2.ObjectIterator(bucket), 10):
            print(b)
        object_meta = bucket.get_object_meta('data_img/ac6eddc451da81cbc77979445e66d01608243198.jpg')
        print(object_meta.headers,"BBBBBBBBBBBB")
        pass




        # https://help.aliyun.com/document_detail/32027.html?spm=a2c4g.11186623.6.828.5f995fffUmP80M