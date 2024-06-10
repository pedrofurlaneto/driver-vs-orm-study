from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_orm.model_sqlalchemy import Base, OrderDetail

class OrderDetailsDAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_order_details(self, order_details_data):
        session = self.Session()
        try:
            order_detail = OrderDetail(
                orderid=order_details_data['orderid'],
                productid=order_details_data['productid'],
                unitprice=order_details_data['unitprice'],
                quantity=order_details_data['quantity'],
                discount=order_details_data['discount']
            )
            session.add(order_detail)
            session.commit()
        except Exception as e:
            session.rollback()
            print("save_order_details", e)
        finally:
            session.close()
