import gevent
import requests
from gevent import monkey
from django.core.management.base import BaseCommand
monkey .patch_all()

class Command(BaseCommand):
    url = 'https://www.qqc-home.com/t_gevent'

    def handle(self, *args, **options):
        self.run()



    def make_data(self,num):
        data={
            'id':num,
            'name':'test'+num
        }
        return data

    @staticmethod
    def run():
        res=requests.get('http://127.0.0.1:8000/t_gevent')
        print(res.json())