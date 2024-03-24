import psycopg
from contextlib import contextmanager

from appdata_postgresql import *


@contextmanager
def create_connection():
    """ create a database connection to a PostgreSQL database """
    connection = psycopg.connect(dbname=DB_NAME_POSTGRESQL, 
        user=USER_POSTGRESQL, 
        password=PASSWORD_POSTGRESQL, 
        host=HOST_POSTGRESQL, 
        port=PORT_POSTGRESQL)
    cursor = connection.cursor()
    cursor.execute('select \'Hello World\'')
    yield connection
    connection.rollback()
    connection.close()