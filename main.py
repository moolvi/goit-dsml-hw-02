import psycopg

from appdata_postgresql import *


def read_file_sql(file_sql):
    read_content = ""
    with open(file_sql, "r") as action:
        read_content = action.read()
    return read_content

def execute_query(query):
    """ create a database connection to a PostgreSQL database """
    with psycopg.connect(CONNINFO) as connection:
        result = connection.execute(query)

def create_tables():
    for script in LIST_SQL_SCRIPTS_CREATE:
        execute_query(read_file_sql(script))

def drop_tables():
    for script in LIST_SQL_SCRIPTS_DROP:
        execute_query(read_file_sql(script))


if __name__ == '__main__':
    print(create_tables())
    print()
    print(drop_tables())