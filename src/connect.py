import psycopg

def connect_database():
    try:
        database_connection = psycopg.connect(
            host='localhost',
            dbname='northwind',
            user = 'northwind_user',
            password = 'northwind',
            autocommit = False
        )

        return database_connection
    except psycopg.OperationalError as e:
        print(e)


DATA_BASE_CONNECTION_STRING = 'postgresql://northwind_user:northwind@localhost:5432/northwind'
