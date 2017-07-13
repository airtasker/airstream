import boto3
import json
import base64
import unittest
import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(os.path.join('..')))
from moto import mock_kinesis
from moto import mock_lambda
from moto import mock_dynamodb2
from event_queue_processing import handler
from mock_event_queue import mock_event_queue
from mock_airgun_lookup_table import mock_airgun_lookup_table
from create_user_queue import create_user_stream

@mock_dynamodb2
@mock_kinesis
@mock_lambda
class TestEventQueueProcessing(unittest.TestCase):
    def test_event_queue_lookup(self):
        dynamo_conn = boto3.client('dynamodb', region_name='ap-southeast-2')
        kinesis_conn = boto3.client('kinesis', region_name='ap-southeast-2')
        mock_airgun_lookup_table(dynamo_conn)
        create_user_stream(kinesis_conn)

        data = 'eyJldmVudF9pZCI6MjU5MiwiZXZlbnRfdHlwZSI6InNlYXJjaC91c2VyIiwiZXZlbnRfY29udGV4dCI6InVwZGF0ZV91c2VyIiwiZXZlbnRfcGF5bG9hZCI6eyJpbmRleF9uYW1lIjoidXNlcnNfaW5kZXhfMjAxNzAzMzAwMDE3MTQ3NjIiLCJkYXRhIjp7ImlkIjoyNTkyLCJmaXJzdF9uYW1lIjoiSGVsbG8iLCJsYXN0X25hbWUiOiJUZXQiLCJuYW1lIjoiSGVsbG8gVGV0IiwiZW1haWwiOiJ0ZXN0MHgzMEB0ZXN0LmNvbSIsInBheXBhbF9lbWFpbCI6bnVsbCwibW9iaWxlIjoiNjY2NjY2NjY2NiIsInZlcmlmaWFibGVfbW9iaWxlIjpudWxsLCJkZXNjcmlwdGlvbiI6ImZkZmRnZ2RnZHNnZGdnZyIsInNsdWciOiJoZWxsby10LTI2NDIzOCIsImRlbGV0ZWRfYXQiOm51bGwsImNyZWF0ZWRfYXQiOiIyMDE3LTA1LTI1VDEwOjMwOjQ3KzEwOjAwIiwidXBkYXRlZF9hdCI6IjIwMTctMDYtMDZUMTE6NDA6MTMrMTA6MDAifX19'

        event = {
            "Records": [
                {
                    "kinesis": {
                        "partitionKey": "user",
                        "kinesisSchemaVersion": "1.0",
                        "data": data,
                        "sequenceNumber": '1'
                    },
                    "eventSource": "aws:kinesis",
                    "eventID": 'shardId-000000000004',
                    "invokeIdentityArn": "arn:aws:iam::account-id:role/testLEBRole",
                    "eventVersion": "1.0",
                    "eventName": "aws:kinesis:record",
                    "eventSourceARN": "arn:aws:kinesis:ap-southeast-2:35667example:stream/examplestream",
                    "awsRegion": "ap-southeast-2"
                }
            ]
        }

        event_context = 'update_user'
        event_handler = handler(event, event_context)
        self.assertEqual(event_handler, "Successfully processed 1 records.")
