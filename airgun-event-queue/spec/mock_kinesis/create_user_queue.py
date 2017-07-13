import sys
sys.dont_write_bytecode = True

def create_user_stream(conn):
    stream = conn.create_stream(
        StreamName='UpdateUser',
        ShardCount=5
    )
    stream_info = conn.describe_stream(
        StreamName='UpdateUser',
        Limit=5
    )
    return stream_info
