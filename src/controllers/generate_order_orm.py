from models.create_order_details import create_order_details
from models.model_orm.customers_dao_orm import CustomerDAO
from models.model_orm.employee_dao_orm import EmployeeDAO
from models.model_orm.order_dao_orm import OrderDAO
from models.model_orm.products_dao_orm import ProductDAO
from models.model_orm.order_details_dao_orm import OrderDetailsDAO
from connect import DATA_BASE_CONNECTION_STRING


def generate_order_orm(product_id, customer_id, quantity, employee_id):
    product_dao = ProductDAO(DATA_BASE_CONNECTION_STRING)
    customer_dao = CustomerDAO(DATA_BASE_CONNECTION_STRING)
    employee_dao = EmployeeDAO(DATA_BASE_CONNECTION_STRING)
    order_dao = OrderDAO(DATA_BASE_CONNECTION_STRING)
    order_details_dao = OrderDetailsDAO(DATA_BASE_CONNECTION_STRING)

    customer = customer_dao.get_customer_by_id(customer_id)
    if customer is None:
        raise Exception('Cliente não encontrado')

    product = product_dao.get_product_by_id(product_id)
    if product is None:
        raise Exception('Produto não encontrado')
    
    if product.unitsinstock - quantity < 0:
        raise Exception('Produto não disponível')

    if not employee_dao.is_employee_valid(employee_id):
        raise Exception("Funcionário não disponível")

    product_dao.update_product_units_in_stock(product_id, quantity)

    order = order_dao.create_order(customer, employee_id)
    order_dao.save_order(order)

    order_details = create_order_details(order.orderid, product, quantity)
    order_details_dao.save_order_details(order_details)
