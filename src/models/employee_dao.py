import psycopg
from connect import connect_database


def is_employee_valid(id: str) -> bool:
    with connect_database() as db_connection:
        session = db_connection.cursor()

        try:
            query = "SELECT * FROM northwind.employees WHERE employeeid = %s"
            session.execute(query, (id,))

            employee = session.fetchone()
            if employee is None:
                return False

            return True

        except psycopg.Error as e:
            print("is_employee_valid", e)