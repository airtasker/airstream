import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/mock_kinesis")
from create_event_queue import create_stream
from put_data_on_the_queue import put_data_on_the_queue

def mock_event_queue(conn):
    stream_info = create_stream(conn)
    put_data_on_the_queue(conn)
