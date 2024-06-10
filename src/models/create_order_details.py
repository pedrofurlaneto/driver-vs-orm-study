from models.dtos.product_dto import Product_DTO


def create_order_details(order_id, product: Product_DTO, quantity):
    return {
        "orderid": order_id,
        "productid": product['productid'],
        "unitprice": product['unitprice'],
        "quantity": quantity,
        "discount": 0
    }


