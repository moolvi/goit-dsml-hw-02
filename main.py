#from psycopg import Error

from connect import create_connection#, database


if __name__ == '__main__':

    with create_connection() as conn:
        if conn is not None:
            pass
        else:
            print("Error! cannot create the database connection.")