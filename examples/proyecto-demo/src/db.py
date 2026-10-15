import os

DB_PASSWORD = 'super-secreto-123'

def get_conn():
    return {'user': 'admin', 'password': DB_PASSWORD}
