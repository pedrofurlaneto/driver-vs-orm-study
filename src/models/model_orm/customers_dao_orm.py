from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_orm.model_sqlalchemy import Base, Customer


class CustomerDAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_customer_by_id(self, customer_id):
        session = self.Session()
        try:
            customer = session.query(Customer).filter_by(customerid=customer_id).first()
            if customer:
                return customer.__dict__
            else:
                print(f"Customer with ID {customer_id} not found.")
                return None
        except Exception as e:
            print("get_customer_by_id error:", e)
        finally:
            session.close()
