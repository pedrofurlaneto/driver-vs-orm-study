from typing import TypedDict


class Product_DTO(TypedDict):
    productid: int
    productname: str
    supplierid: int
    categoryid: int
    quantityperunit: str
    unitprice: float
    unitsinstock: int
    unitsonorder: int
    reorderlevel: int
    discontinued: chr