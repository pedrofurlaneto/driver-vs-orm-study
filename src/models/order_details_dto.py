from typing import TypedDict


class Order_Details_DTO(TypedDict):
    orderid: int
    productid: int
    unitprice: int
    quantity: int
    discount: int
    