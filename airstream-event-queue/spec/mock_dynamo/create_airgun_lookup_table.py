import sys
sys.dont_write_bytecode = True

def create_table(conn):
    table = conn.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'queues',
                'AttributeType': 'SS'
            },
        ],
        TableName='airgun-lookup',
        KeySchema=[
            {
                'AttributeName': 'event_context',
                'KeyType': 'HASH'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table
