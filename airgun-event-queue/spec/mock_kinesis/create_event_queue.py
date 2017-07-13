import sys
sys.dont_write_bytecode = True

def create_stream(conn):
    stream = conn.create_stream(
        StreamName='EventQueue',
        ShardCount=5
    )
    stream_info = conn.describe_stream(
        StreamName='EventQueue',
        Limit=5
    )
    return stream_info
