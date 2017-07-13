import unittest
import json
from elasticsearch import Elasticsearch

def create_user_index(self):
    es = Elasticsearch('localhost:9200')
    index_name = 'users_index_test_20170602112022932'
    doc_type = 'search/user'
    body = {
                 "first_name": "Poster1",
                 "last_name": "One",
                 "name": "Poster",
                 "mobile": "0450346507",
                 "created_at": "2016-10-27T09:13:20+11:00",
                 "updated_at": "2017-06-06T16:59:26+10:00",
                 "id": 915,
                 "email": "poster1@dev.com",
                 "verifiable_mobile": None,
                 "deleted_at": None,
                 "paypal_email": "",
                 "slug": "poster1-o-262642",
                 "description": "Lorem ipsum dolor sit amet"
                }

    data = es.index(index=index_name, doc_type=doc_type, id=915,body=body)
