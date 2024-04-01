HOST_POSTGRESQL = '127.0.0.1'
USER_POSTGRESQL = ''
PASSWORD_POSTGRESQL = ''
DB_NAME_POSTGRESQL = 'task_management_system.db'
PORT_POSTGRESQL = '5432'

CONNINFO = (
    f"host={HOST_POSTGRESQL}"
    f" port={PORT_POSTGRESQL}"
    f" dbname={DB_NAME_POSTGRESQL}"
    f" user={USER_POSTGRESQL}"
    f" password={PASSWORD_POSTGRESQL}"
    )

LIST_SQL_SCRIPTS_CREATE = [
    "create_types.sql",
    "create_table_status.sql",
    "create_table_users.sql",
    "create_table_tasks.sql"
    ]

LIST_SQL_SCRIPTS_DROP = [
    "drop_table_tasks.sql",
    "drop_table_users.sql",
    "drop_table_status.sql",
    "drop_types.sql"
    ]

LIST_SQL_SCRIPTS_QUERIES = [
    "queries.sql",
    ]