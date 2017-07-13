import sys, os
sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/mock_dynamo")
from create_airgun_lookup_table import create_table
from load_data_in_airgun_lookup import load_data_in_dynamo

def mock_airgun_lookup_table(conn):
    create_table(conn)
    load_data_in_dynamo(conn)
