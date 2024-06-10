from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.model_orm.model_sqlalchemy import Base, Order
from models.model_orm.employee_dao_orm import Employee
from models.model_orm.order_details_dao_orm import OrderDetail
from sqlalchemy import func, desc

class OrderDAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_order(self, order_data):
        session = self.Session()
        try:
            order = Order(
                orderid=order_data["orderid"],
                customerid=order_data["customerid"],
                employeeid=order_data["employeeid"],
                orderdate=datetime.strptime(order_data["orderdate"], '%Y-%m-%d'),
                requireddate=datetime.strptime(order_data["required_date"], '%Y-%m-%d'),
                freight=order_data["freight"],
                shipname=order_data["shipname"],
                shipaddress=order_data["shipaddress"],
                shipcity=order_data["shipcity"],
                shipcountry=order_data["shipcountry"]
            )
            session.add(order)
            session.commit()
        except Exception as e:
            session.rollback()
            print("save_order", e)
        finally:
            session.close()

    def create_order(self, customer, employee_id):
        session = self.Session()
        try:
            # Assuming orders are already in the database and orderid is autoincremented
            last_order = session.query(Order).order_by(Order.orderid.desc()).first()
            last_id = last_order.orderid if last_order else 0
            order_data = {
                "orderid": last_id + 1,
                "customerid": customer["customerid"],
                "employeeid": employee_id,
                "orderdate": "2024-03-25",
                "required_date": "2024-04-25",
                "freight": 10,
                "shipname": customer["contactname"],
                "shipaddress": customer["address"],
                "shipcity": customer["city"],
                "shipcountry": customer["country"]
            }
            self.save_order(order_data)
            return order_data
        except Exception as e:
            session.rollback()
            print("create_order", e)
        finally:
            session.close()

    def get_order_by_id(self, order_id):
        session = self.Session()
        try:
            order = session.query(Order).filter_by(orderid=order_id).first()
            if order:
                return order.__dict__
            else:
                print(f"Order with ID {order_id} not found.")
                return None
        except Exception as e:
            print("get_order_by_id error:", e)
        finally:
            session.close()

def get_employee_ranking(self, start_date, end_date):
        session = self.Session()
        ranking = session.query(
            Employee.firstname,
            Employee.lastname,
            func.count(Order.orderid).label('total_orders'),
            func.sum(OrderDetail.unitprice * OrderDetail.quantity).label('total_sales')
        ).join(Order).join(OrderDetail).filter(
            Order.orderdate.between(start_date, end_date)
        ).group_by(Employee.firstname, Employee.lastname).order_by(desc('total_sales')).all()
        session.close()
        return ranking
