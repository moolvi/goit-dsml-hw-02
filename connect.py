import psycopg
from contextlib import contextmanager

from appdata_postgresql import *


@contextmanager
def create_connection():
    """ create a database connection to a PostgreSQL database """
    with psycopg.connect(dbname=DB_NAME_POSTGRESQL, 
        user=USER_POSTGRESQL, 
        password=PASSWORD_POSTGRESQL, 
        host=HOST_POSTGRESQL, 
        port=PORT_POSTGRESQL) as connection:
        #yield connection
        try:
            yield connection
        except BaseException:
            connection.rollback()
        else:
            connection.commit()
        finally:
            connection.close()