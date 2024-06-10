from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_orm.model_sqlalchemy import Base, Employee

class EmployeeDAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def is_employee_valid(self, employee_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter_by(employeeid=employee_id).first()
            return employee is not None
        except Exception as e:
            print("is_employee_valid error:", e)
            return False
        finally:
            session.close()
