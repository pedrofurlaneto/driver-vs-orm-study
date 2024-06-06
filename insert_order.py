import psycopg
from connect import connect_database

def insert_order(product_id, quantity):
    units_in_stock = get_product_units_in_stock

    if units_in_stock - quantity > 0:
        update_product_units_in_stock(product_id, units_in_stock)
        return


def update_product_units_in_stock(product_id, units):
    with connect_database() as db_connection:
        session = db_connection.cursor()

        with db_connection.transaction as savepoint1:
            try:
                update_stock_units_query = "UPDATE northwind.products SET unitsinstock = %s WHERE productid = %s"

                session.execute(update_stock_units_query, (product_id, units))
                print("estoque atualizado")

            except psycopg.OperationalError as e:
                print("update_product_units_in_stock error", e)
                raise psycopg.Rollback(savepoint1)


def get_product_units_in_stock(product_id):
    with connect_database() as db_connection:
        try:
            session = db_connection.cursor()

            get_product_units_query = (
                "SELECT unitsinsotck FROM northwind.products WHERE productid = %s"
            )
            session.execute(get_product_units_query, (product_id))

            return int(session.fetchone()[0])

        except psycopg.OperationalError as e:
            print("get_product_units_in_stock error", e)


def create_order(): ...
def associate_order_and_product(): ...

