import psycopg
from connect import connect_database
from models.customer_dto import Customer_DTO
from models.order_dto import Order_DTO


def save_order(order: Order_DTO):
    with connect_database() as db_connection:
        session = db_connection.cursor()

        with db_connection.transaction() as savepoint:
            try:
                query = "INSERT INTO northwind.orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                session.execute(
                    query,
                    (
                        order["orderid"],
                        order["customerid"],
                        order["employeeid"],
                        order["orderdate"],
                        order["required_date"],
                        None,
                        order["freight"],
                        order["shipname"],
                        order["shipaddress"],
                        order["shipcity"],
                        None,
                        None,
                        order["shipcontry"],
                        None,
                    ),
                )

            except psycopg.Error as e:
                print("save_order", e)

                raise psycopg.Rollback(savepoint)


def create_order(customer: Customer_DTO, employee_id: int) -> Order_DTO:
    with connect_database() as db_connection:
        session = db_connection.cursor()
        select_query = "SELECT * from northwind.orders ORDER BY orderid DESC"

        session.execute(select_query)
        last_id = session.fetchone()[0]

        return {
            "orderid": last_id + 1,
            "customerid": customer["customerid"],
            "employeeid": employee_id,
            "orderdate": "2024-03-25",
            "required_date": "2024-04-25",
            "freight": 10,
            "shipname": customer["contactname"],
            "shipaddress": customer["address"],
            "shipcity": customer["city"],
            "shipcontry": customer["country"],
        }
