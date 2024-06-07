import psycopg
from connect import connect_database
from parse_dao_to_dto import parse_DAO_to_DTO_list
from order_dto import Order_DTO


def get_costumer_by_id(id: str) -> Order_DTO:
    with connect_database() as db_connection:
        session = db_connection.cursor()

        try:
            query = "SELECT * FROM northwind.customers WHERE customerid = %s"
            session.execute(query, (id,))

            if session.fetchone() is None:
                return None

            return parse_DAO_to_DTO_list(session)

        except psycopg.Error as e:
            print("get_costumer_by_id", e)