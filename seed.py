import psycopg

from faker import Faker
from datetime import datetime
from random import randint, choice

from appdata_postgresql import *

NUMBER_FULLNAME = 50
NUMBER_EMAIL = 50
NUMBER_TITLE = 50
NUMBER_DESCRIPTION = 50
# NUMBER_STATUS = 3

def generate_fake_data(NUMBER_FULLNAME, NUMBER_EMAIL, NUMBER_TITLE, NUMBER_DESCRIPTION) -> tuple():
    fake_fullname = []
    fake_email = []
    fake_title = []
    fake_description = []
    fake_status = []
    enum_status = [('new',), ('in progress',), ('completed',)]
    
    fake_data = Faker('uk-UA')

    for _ in range(NUMBER_FULLNAME):
        fake_fullname.append(fake_data.name())

    for _ in range(NUMBER_EMAIL):
        fake_email.append(fake_data.email())
    
    # for status in enum_status:
    #     fake_status.append(status)
    fake_status = enum_status

    for _ in range(NUMBER_TITLE):
        fake_title.append(fake_data.bothify(text = '?????-#######'))
    
    for _ in range(NUMBER_DESCRIPTION):
        fake_description.append(fake_data.text())

    return fake_fullname, fake_email, fake_status, fake_title, fake_description

def prepare_data(fullnames, emails, statuses, titles, descriptions) -> tuple():
    for_users = []
    for a in range(len(fullnames)):
        for_users.append((fullnames[a], emails[a]))

    # for_statuses = []
    # for status in range(statuses):
    #     for_statuses.append((status,))
    for_statuses = statuses

    for_tasks = []
    for a in range(len(titles)):
        for_tasks.append((titles[a], choice(descriptions), randint(1, len(for_statuses)), randint(1, len(for_users))))

    return for_users, for_statuses, for_tasks


def insert_data_to_db(users, statuses, tasks) -> None:
    sql_to_users = "INSERT INTO users (fullname, email) VALUES (%s, %s)"
    with psycopg.connect(CONNINFO) as connection:
        for user in users:
            connection.execute(sql_to_users, user)

    sql_to_statuses = "INSERT INTO status (name) VALUES (%s)"
    with psycopg.connect(CONNINFO) as connection:
        for status in statuses:
            connection.execute(sql_to_statuses, status)

    sql_to_tasks = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
    with psycopg.connect(CONNINFO) as connection:
        for task in tasks:
            connection.execute(sql_to_tasks, task)