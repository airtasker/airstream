import boto3
from boto3.dynamodb.conditions import Key, Attr

def queues_lookup(dynamo_client, event_context_value):
    response = dynamo_client.get_item(TableName='airgun-lookup', Key={'event_context':{'S': str(event_context_value)}})
    if 'Item' in response:
        return response['Item']
    else:
        return "No queues found"
