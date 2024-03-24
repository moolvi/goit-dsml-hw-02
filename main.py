import psycopg

from connect import *


def read_file_sql(file_sql):
    with open(file_sql, "r") as action:
        read_content = action.read()
    return read_content

def execute_query(connection, query):
    temp = connection.execute(query)
    #return cursor.fetchone()



if __name__ == '__main__':

    with create_connection() as connection:
        if connection is not None:
            temp1 = read_file_sql('create_types.sql')
            print(execute_query(connection, temp1))
        else:
            print("Error! cannot create the database connection.")