import psycopg
from connect import connect_database
from models.utils.parse_dao_to_dto import parse_DAO_to_DTO_list
from models.dtos.customer_dto import Customer_DTO


def get_customer_by_id(id: str) -> Customer_DTO:
    with connect_database() as db_connection:
        session = db_connection.cursor()

        try:
            query = "SELECT * FROM northwind.customers WHERE customerid = %s"
            session.execute(query, (id,))

            costumer = session.fetchone()
            if costumer is None:
                return None

            return parse_DAO_to_DTO_list(session.description, [costumer])[0]

        except psycopg.Error as e:
            print("get_costumer_by_id", e)