from typing import TypedDict


class Order_DTO(TypedDict):
    orderid: int
    customerid: str
    employeeid: int
    orderdate: str
    required_date: str
    freight: float
    shipname: str
    shipaddress: str
    shipcity: str
    shipcontry: str