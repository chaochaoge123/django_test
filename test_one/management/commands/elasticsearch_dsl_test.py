from datetime import datetime
from elasticsearch_dsl import document, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Integer, DocType
from elasticsearch_dsl.connections import connections
from test_one .models .user import User_info

connections .create_connection(hosts=['172.29.32.104'])
