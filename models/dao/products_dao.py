import psycopg
from connect import connect_database
from models.dao.utils.parse_dao_to_dto import parse_DAO_to_DTO_list

def update_product_units_in_stock(product_id: int, units: int):
    with connect_database() as db_connection:
        session = db_connection.cursor()

        with db_connection.transaction() as savepoint:
            try:
                update_stock_units_query = "UPDATE northwind.products SET unitsinstock = %s WHERE productid = %s"

                session.execute(update_stock_units_query, (product_id, units))
                print("Estoque atualizado")

            except psycopg.Error as e:
                print("update_product_units_in_stock error", e)
                raise psycopg.Rollback(savepoint)


def get_product_by_id(id: int):
    with connect_database() as db_connection:
        try:
            session = db_connection.cursor()

            query = "SELECT * FROM northwind.products WHERE productid = %s"
            session.execute(query, (id,))

            return parse_DAO_to_DTO_list(session)[0]

        except psycopg.Error as e:
            print("get_product_units_in_stock error", e)