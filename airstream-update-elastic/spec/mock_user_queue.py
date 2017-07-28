import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/mock_kinesis")
from create_user_queue import create_user_stream
from put_data_on_the_queue import put_data_on_the_queue

def mock_user_queue(conn):
    stream_info = create_user_stream(conn)
    put_data_on_the_queue(conn)
