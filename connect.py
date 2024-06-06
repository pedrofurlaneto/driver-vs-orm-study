import psycopg

def connect_database():
    try:
        database_connection = psycopg.connect(
            host='localhost',
            dbname='postgres',
            user = 'postgres',
            password = 'postgres'
        )

        print('Banco conectado')

        return database_connection
    except Exception as e:
        print(e)