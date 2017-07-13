import sys
sys.dont_write_bytecode = True

def load_data_in_dynamo(conn):
    response = conn.batch_write_item(
        RequestItems={
            'airgun-lookup': [
                {
                    'PutRequest': {
                        'Item': {
                            'event_context': {
                                'S': 'create_user',
                            },
                            'queues': {
                                'SS': ['CreateUser'],
                            },
                        },
                    },
                },
                {
                    'PutRequest': {
                        'Item': {
                            'event_context': {
                                'S': 'update_user',
                            },
                            'queues': {
                                'SS': ['UpdateUser'],
                            },
                        },
                    },
                },
            ],
        },
    )
