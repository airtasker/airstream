from __future__ import print_function

import base64
import json
import boto3
import os
from elasticsearch import Elasticsearch

print('Loading function')

def lambda_handler(event, context):
    es = Elasticsearch(os.environ['ELASTICSEARCH_URL'])
    indices_list = es.indices.get('*')
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        update_object_payload = json.loads(payload)
        doc_type_name = update_object_payload['event_type']
        index_name = update_object_payload['event_payload']['index_name']
        payload_data = update_object_payload['event_payload']['data']

        index_terms = index_name.split('_')
        del index_terms[-1]
        index_prefix = '_'.join(index_terms)
        latest_index_name = max(filter(lambda k: index_prefix in k, indices_list))
        if latest_index_name != index_name:
            index_name = latest_index_name

        res = es.update(index=index_name, doc_type=doc_type_name, id=str(update_object_payload['object_id']), body={'doc': payload_data, 'doc_as_upsert':True})

    for conn in es.transport.connection_pool.connections:
        conn.pool.close()

    return 'Successfully processed {} records.'.format(len(event['Records']))
