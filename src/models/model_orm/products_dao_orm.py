from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_orm.model_sqlalchemy import Base, Product

class ProductDAO:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def update_product_units_in_stock(self, product_id, units):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(productid=product_id).first()
            if product:
                product.unitsinstock = units
                session.commit()
                print("Estoque atualizado")
            else:
                print(f"Produto com ID {product_id} não encontrado.")
        except Exception as e:
            session.rollback()
            print("update_product_units_in_stock error:", e)
        finally:
            session.close()

    def get_product_by_id(self, product_id):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(productid=product_id).first()
            if product:
                return product.__dict__
            else:
                print(f"Produto com ID {product_id} não encontrado.")
                return None
        except Exception as e:
            print("get_product_by_id error:", e)
        finally:
            session.close()
