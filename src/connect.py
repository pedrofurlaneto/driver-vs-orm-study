import psycopg

def connect_database():
    try:
        database_connection = psycopg.connect(
            host='localhost',
            dbname='bd2',
            user = 'postgres',
            password = 'postgres',
            autocommit = False
        )

        return database_connection
    except psycopg.OperationalError as e:
        print(e)


DATA_BASE_CONNECTION_STRING = 'postgresql://postgres:postgres@localhost:5432/bd2'
