#!/usr/bin/env python
# encoding: utf-8

import redis
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

        # 创建索引
        # ret = es.indices.create(index="one")
        # print(es.indices.delete(index="one"),"KKKKKKKKKKKKK")
        # print(ret)

        # 只查询id和type
        # print(es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type']))
        # 通配符* 过滤
        # print(es.search(index='test-index', filter_path=['hits.hits._*']))

        # 获取集群信息
        # print(es.info())

        # 获取集群所有索引
        print(es.cat.indices())

        # print(es.cat.nodes())
        # print(es.cat.health())
        # print(es.tasks.list())

        #插入数据
        # res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
        # print(res, "###########################")
        # print(res['result'])

        # res = es.get(index="test-index", doc_type='tweet', id=1)
        # print(res,"%%%%%%%%%%%%%%%%%%%%%%%200")
        # print(res['_source'])
        #
        # es.indices.refresh(index="test-index")
        #
        # res = es.search(index="test-index", body={"query": {"match_all": {}}})
        # print(res,"@@@@@@@@@@@@@@@@@@@@@@")
        # print("Got %d Hits:" % res['hits']['total']['value'])
        # for hit in res['hits']['hits']:
        #     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

        # dict格式搜索
        response = es.search(
            index="my-index",
            body={
                "query": {
                    "filtered": {
                        "query": {
                            "bool": {
                                "must": [{"match": {"title": "python"}}],
                                "must_not": [{"match": {"description": "beta"}}]
                            }
                        },
                        "filter": {"term": {"category": "search"}}
                    }
                },
                "aggs": {
                    "per_tag": {
                        "terms": {"field": "tags"},
                        "aggs": {
                            "max_lines": {"max": {"field": "lines"}}
                        }
                    }
                }
            }
        )

        print(response,"++++++++++++++++++")