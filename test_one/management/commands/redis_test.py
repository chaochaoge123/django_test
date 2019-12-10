#!/usr/bin/env python
# encoding: utf-8

import redis
from django.core.management.base import BaseCommand
from django.shortcuts import render,HttpResponse

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_xf_user()

    @staticmethod
    def add_xf_user():
        r = redis.Redis(host='47.102.138.171', port=6379, password="qqcqqc")
        r.set('age',99)
        print(r.get("age"),"KKKKKKKKKKKKKK")


