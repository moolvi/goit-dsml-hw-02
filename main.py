import psycopg
import re

from seed import *
from appdata_postgresql import *


def read_file_sql(file_sql):
    read_content = ""
    with open(file_sql, "r") as action:
        read_content = action.read()
    return read_content

def execute_query(query):
    result = ''
    with psycopg.connect(CONNINFO) as connection:
        try:
            result = f'{connection.execute(query).fetchall()}\n'
        except:
            result = None
    return result

def create_tables():
    """ create a database connection to a PostgreSQL database """
    for script in LIST_SQL_SCRIPTS_CREATE:
        execute_query(read_file_sql(script))

def drop_tables():
    for script in LIST_SQL_SCRIPTS_DROP:
        execute_query(read_file_sql(script))

def queries_tables():
    result =''
    for file in LIST_SQL_SCRIPTS_QUERIES:
        queries = read_file_sql(file).split('\n')
        for query in queries:
            result = f'{result}\n{execute_query(query)}'
    return result


if __name__ == '__main__':
    # print(drop_tables())
    # print(create_tables())

    # fake_fullname, fake_email, fake_title, fake_description = generate_fake_data(NUMBER_FULLNAME, NUMBER_EMAIL, NUMBER_TITLE, NUMBER_DESCRIPTION)
    # print()

    # for_users, for_statuses, for_tasks = prepare_data(*generate_fake_data(NUMBER_FULLNAME, NUMBER_EMAIL, NUMBER_TITLE, NUMBER_DESCRIPTION))
    # insert_data_to_db(for_users, for_statuses, for_tasks)
    print(queries_tables())