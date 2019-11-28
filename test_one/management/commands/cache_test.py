#!/usr/bin/env python
# encoding: utf-8

import redis
from django.core.management.base import BaseCommand
from django.shortcuts import render,HttpResponse
from django.core.cache import cache

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_cache()

    @staticmethod
    def add_cache():
        print(cache.get("add"))
