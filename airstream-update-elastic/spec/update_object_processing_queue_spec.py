import boto3
import json
import base64
import unittest
import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(os.path.join('..')))
from mock_user_queue import mock_user_queue
from mock_user_elastic_index import create_user_index
from update_object_processing_queue import lambda_handler

class TestUserObjectProcessing(unittest.TestCase):
    def setUp(self):
        create_user_index(self)

    def test_user_update(self):
        data = "eyJldmVudF9jb250ZXh0IjogInVwZGF0ZV91c2VyIiwgImV2ZW50X3BheWxvYWQiOiB7ImRhdGEiOiB7ImNyZWF0ZWRfYXQiOiAiMjAxNi0xMC0yN1QwOToxMzoyMCsxMTowMCIsICJmaXJzdF9uYW1lIjogIlBvc3RlcjEiLCAibGFzdF9uYW1lIjogIk9uZSIsICJuYW1lIjogIlBvc3RlcjEgT25lIiwgIm1vYmlsZSI6ICIwNDUwMzQ2NTA3IiwgInNsdWciOiAicG9zdGVyMS1vLTI2MjY0MiIsICJ1cGRhdGVkX2F0IjogIjIwMTctMDYtMDZUMTY6NTk6MjYrMTA6MDAiLCAiaWQiOiA5MTUsICJ2ZXJpZmlhYmxlX21vYmlsZSI6IG51bGwsICJkZWxldGVkX2F0IjogbnVsbCwgInBheXBhbF9lbWFpbCI6ICIiLCAiZW1haWwiOiAicG9zdGVyMUBkZXYuY29tIiwgImRlc2NyaXB0aW9uIjogIkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LCBjb25zZWN0ZXR1ciBhZGlwaXNjaW5nIGVsaXQuIEV0aWFtIGp1c3RvIGFyY3UsIGV1aXNtb2QgYWMgZGlhbSBub24sIHZvbHV0cGF0IGZldWdpYXQgbmlzbC4gVXQgc29kYWxlcyB0ZW1wb3IgbWFnbmEsIHV0IGF1Y3RvciBkdWkgYWNjdW1zYW4gZXUuIEFsaXF1YW0gZXUgbWFnbmEgbm9uIHR1cnBpcyBmaW5pYnVzIGJpYmVuZHVtIHNpdCBhbWV0IHNpdCBhbWV0IGRpYW0uIEV0aWFtIGF0IGxpZ3VsYSBudW5jLiBDdXJhYml0dXIgc2VkIGNvbnZhbGxpcyBleC4gSW4gaWQgYmliZW5kdW0gbmlzbC4gQ3VyYWJpdHVyIGV1IHVybmEgbWF1cmlzLiBWZXN0aWJ1bHVtIGFudGUgaXBzdW0gcHJpbWlzIGluIGZhdWNpYnVzIG9yY2kgbHVjdHVzIGV0IHVsdHJpY2VzIHBvc3VlcmUgY3ViaWxpYSBDdXJhZTsgTW9yYmkgZmV1Z2lhdCBtaSBpZCB1bHRyaWNlcyBtb2xlc3RpZS4gU2VkIGJsYW5kaXQgdXQgbmlzaSBzZWQgdHVycGlzIGR1aXMuIG5hbmFubmFcbkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LCBjb25zZWN0ZXR1ciBhZGlwaXNjaW5nIGVsaXQuIER1aXMgcnV0cnVtIGZlbGlzIHZpdGFlIG9kaW8gYmxhbmRpdCwgZWdldCBzYWdpdHRpcyBsZWN0dXMgdmVzdGlidWx1bS4gSW50ZWdlciBydXRydW0gbnVsbGEgaWQgZGlhbSBjb25zZWN0ZXR1ciwgYXQgdGluY2lkdW50IHNhcGllbiB2b2x1dHBhdC4gTnVsbGFtIGJsYW5kaXQgZGlnbmlzc2ltIGZldWdpYXQuIE1hZWNlbmFzIHJpc3VzIGFudGUsIGZldWdpYXQgc2l0IGFtZXQgbnVsbGEgc2VkLCBmcmluZ2lsbGEgbnVsbGFtLiJ9LCAiaW5kZXhfbmFtZSI6ICJ1c2Vyc19pbmRleF8yMDE3MDMzMDAwMTcxNDc2MiJ9LCAiZXZlbnRfdHlwZSI6ICJzZWFyY2gvdXNlciIsICJvYmplY3RfaWQiOiA5MTV9"

        event = {
            "Records": [
                {
                    "eventVersion": "1.0",
                    "eventID": "shardId-000000000002:49571080450396445196975177680178116050521945325053149218",
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

        event_context = "update_user"
        response = lambda_handler(event, event_context)
        self.assertEqual(response, "Successfully processed 1 records.")
