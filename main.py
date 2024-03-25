import psycopg

from seed import *
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
    print(drop_tables())
    print(create_tables())

    # fake_fullname, fake_email, fake_title, fake_description = generate_fake_data(NUMBER_FULLNAME, NUMBER_EMAIL, NUMBER_TITLE, NUMBER_DESCRIPTION)
    # print()

    for_users, for_statuses, for_tasks = prepare_data(*generate_fake_data(NUMBER_FULLNAME, NUMBER_EMAIL, NUMBER_TITLE, NUMBER_DESCRIPTION))
    insert_data_to_db(for_users, for_statuses, for_tasks)