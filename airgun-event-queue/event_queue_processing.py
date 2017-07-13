from __future__ import print_function

import base64
import json
import boto3
from queues_lookup import queues_lookup

print('Loading function')

def handler(event, context):
    kinesis_client = boto3.client('kinesis')
    dynamo_client = boto3.client('dynamodb')

    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        event_payload = json.loads(payload)
        new_payload = {}
        new_payload['object_id'] = event_payload['event_id']
        new_payload['event_type'] = event_payload['event_type']
        new_payload['event_context'] = event_payload['event_context']
        new_payload['event_payload'] = event_payload['event_payload']

        dynamo_response = queues_lookup(dynamo_client, event_payload["event_context"])

        if dynamo_response != "No queues found":
            for res in dynamo_response['queues']['SS']:
                kinesis_response = kinesis_client.put_record(
                    StreamName=str(res),
                    Data=json.dumps(new_payload),
                    PartitionKey=record['kinesis']['partitionKey']
                )

    return 'Successfully processed {} records.'.format(len(event['Records']))
