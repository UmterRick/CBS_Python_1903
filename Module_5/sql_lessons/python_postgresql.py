import psycopg2
from psycopg2 import OperationalError


database="sql_essential_db"
user="student"
password="cyberbionics"
host="127.0.0.1"
port=5432


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


connection = create_connection(
    db_name=database,
    db_user=user,
    db_password=password,
    db_host=host,
    db_port=port
)


if __name__ == "__main__":
    query = """
    SELECT *
    FROM customers;
    """

    query_result = execute_read_query(
        connection=connection,
        query=query
    )

    for record in query_result:
        print(record)


