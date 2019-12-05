#!/usr/bin/env python
# encoding: utf-8

import redis
import json
from test_one.models.user import User_info,Item
from django.core.management.base import BaseCommand
from django.shortcuts import render,HttpResponse
from django.core.cache import cache
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
es = Elasticsearch(hosts=['172.29.32.104:9200'])
es_dsl = Search(using=es)

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.add_es()

    @staticmethod
    def add_es():
        doc = {
            'author': 'qqc',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }
        data = {'name': 'hello',
                'mobile': '2367299',
                'remark': '明月'}

        # 创建索引
        # ret = es.indices.create(index="two")
        # print(es.delete(index="one"),"KKKKKKKKKKKKK")
        # print(ret)

        # 只查询id和type
        # print(es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._source']))
        # 通配符* 过滤
        # print(es.search(index='test-index', filter_path=['hits.hits._source']))

        # 获取集群信息
        # print(es.info())

        # 获取集群所有索引
        print(es.cat.indices())

        # print(es.cat.nodes())
        # print(es.cat.health())
        # print(es.tasks.list())

        #插入数据
        # res = es.index(index="test-index", doc_type='tweet', id=1, body=data)
        # res = es.index(index='one',doc_type='ones', id=2, body=data)
        #
        # print(res, "###########################")
        # print(res['result'])

        # res = es.get(index="test-index", doc_type='tweet', id=1)
        # print(res,"%%%%%%%%%%%%%%%%%%%%%%%200")
        # print(res['_source'])
        #
        # print(es.indices.refresh(index="one"),"MMMMMMMMMMMM")
        #
        # 循环取值
        # https://blog.csdn.net/qq_41782425/article/details/90720889
        print(es.search(index="test-index", body={"query": {"match_all": {}}})) # 查所有数据
        # res = es.search(index="test-index", body={"query": {"match": {"name":"erww"}}}) # 查询name是er(包含)的数据
        # res =es.search(index="test-index", body={"query": {"terms": {"text": ["er","100"]}}})

        # print(res,"@@@@@@@@@@@@@@@@@@@@@@")
        # print("Got %d Hits:" % res['hits']['total']['value'])
        # mo ='user_info'
        # for hit in res['hits']['hits']:
        #     if hit['_id'].split('.')[1] == mo:
        #         print(hit['_source'])

        # mapping

        # print(response,"++++++++++++++++++")