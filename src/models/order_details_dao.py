import psycopg
from connect import connect_database
from models.dtos.order_details_dto import Order_Details_DTO


def save_order_details(order_details: Order_Details_DTO):
    with connect_database() as db_connection:
        session = db_connection.cursor()

        with db_connection.transaction() as savepoint:
            try:
                query = "INSERT INTO northwind.order_details VALUES(%s, %s, %s, %s, %s)"

                print(order_details['orderid'])

                session.execute(query, (order_details['orderid'], order_details['productid'], order_details['unitprice'], order_details['quantity'], order_details['discount']))
            except psycopg.Error as e:
                print('save_order_details', e)

                raise psycopg.Rollback(savepoint)