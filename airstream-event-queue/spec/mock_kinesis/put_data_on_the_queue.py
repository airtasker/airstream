import json
import sys
sys.dont_write_bytecode = True

def put_data_on_the_queue(conn):
    payload_data = {}
    payload_data['id'] = 30
    payload_data['first_name'] = 'John'
    payload_data['last_name'] = 'Doe'
    payload_data['name'] = 'John Doe'
    payload_data['email'] = 'john.doe@gmail.com'
    payload_data['paypal_email'] = 'john.doe@gmail.com'
    payload_data['mobile'] = '0415000111'
    payload_data['verifiable_mobile'] = '0415000111'
    payload_data['description'] = 'description'
    payload_data['slug'] = 'john-doe-30'
    payload_data['deleted_at'] = '2017-04-12 17:29:37 +1000'
    payload_data['created_at'] = '2017-04-12 16:29:22 +1000'
    payload_data['created_at'] = '2017-04-12 16:29:22 +1000'

    data = {
        'event_id': 20,
        'event_type': 'search/user',
        'event_context': 'create_user',
        'event_payload': {
            "index_name": "users_index_20170316114320429",
            "data": payload_data
        }
    }

    response = conn.put_record(
        StreamName='EventQueue',
        Data=str(data),
        PartitionKey='user'
    )
    return response
