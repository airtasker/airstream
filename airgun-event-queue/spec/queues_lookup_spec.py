import boto3
import json
from moto import mock_dynamodb2
import unittest
import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(os.path.join('..')))
from queues_lookup import queues_lookup
from mock_airgun_lookup_table import mock_airgun_lookup_table

@mock_dynamodb2
class TestQueuesLookup(unittest.TestCase):
    def test_queue_lookup(self):
        conn = boto3.client('dynamodb', region_name='ap-southeast-2')
        response = conn.list_tables()

        if response["TableNames"].__len__() <= 0:
            mock_airgun_lookup_table(conn)
        event_context = 'create_user'
        queues = queues_lookup(conn, event_context)
        self.assertEqual(queues['event_context']['S'], event_context)
