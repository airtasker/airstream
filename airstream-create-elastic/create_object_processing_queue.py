from __future__ import print_function

import base64
import json
import boto3
import os
from elasticsearch import Elasticsearch

print('Loading function')

def lambda_handler(event, context):
    es = Elasticsearch(os.environ['ELASTICSEARCH_URL'])
    indices = es.indices.get('*')
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        create_object_payload = json.loads(payload)
        doc_type_name = create_object_payload['event_type']
        index_name = create_object_payload['event_payload']['index_name']
        payload_data = create_object_payload['event_payload']['data']

        index_terms = index_name.split('_')
        del index_terms[-1]
        index_prefix = '_'.join(index_terms)
        latest_index_name = max(filter(lambda k: index_prefix in k, indices))
        if latest_index_name != index_name:
            index_name = latest_index_name

        res = es.index(index=index_name, doc_type=doc_type_name, id=str(create_object_payload['object_id']), body=payload_data)
    for conn in es.transport.connection_pool.connections:
        conn.pool.close()

    return 'Successfully processed {} records.'.format(len(event['Records']))
