from models.model_orm.order_dao_orm import OrderDAO
from connect import DATA_BASE_CONNECTION_STRING


def generate_order_data(order_id):
    order_dao = OrderDAO(DATA_BASE_CONNECTION_STRING)
    order = order_dao.get_order_by_id(order_id)
    if order is None:
        raise Exception('Pedido não encontrado')
    return order.__dict__



def generate_employees_data(start_date, end_date):
    order_dao = OrderDAO(DATA_BASE_CONNECTION_STRING)
    return order_dao.get_employee_ranking(start_date, end_date)



