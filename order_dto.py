from typing import TypedDict

class Order_DTO(TypedDict):
    customerid: str
    companyname: str
    contactname: str
    contacttitle: str
    address: str
    city: str
    region: str
    postalcode: str
    country: str
    phone: str
    fax: str