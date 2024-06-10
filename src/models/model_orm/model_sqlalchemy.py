from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}
    
    orderid = Column(Integer, primary_key=True, autoincrement=True)
    customerid = Column(String)
    employeeid = Column(Integer, ForeignKey('northwind.employees.employeeid'))
    orderdate = Column(DateTime)
    requireddate = Column(DateTime)
    shippeddate = Column(DateTime)
    freight = Column(Numeric)
    shipname = Column(String)
    shipaddress = Column(String)
    shipcity = Column(String)
    shipregion = Column(String)
    shippostalcode = Column(String)
    shipcountry = Column(String)
    shipperid = Column(Integer)
    qtdprodutos = Column(Integer)
    maisdesconto = Column(Integer)

    employee = relationship("Employee", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")

class OrderDetail(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}
    
    orderid = Column(Integer, ForeignKey('northwind.orders.orderid'), primary_key=True)
    productid = Column(Integer, ForeignKey('northwind.products.productid'), primary_key=True)
    unitprice = Column(Numeric)
    quantity = Column(Integer)
    discount = Column(Numeric)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'northwind'}
    
    productid = Column(Integer, primary_key=True)
    productname = Column(String)
    supplierid = Column(Integer)
    categoryid = Column(Integer)
    quantityperunit = Column(String)
    unitprice = Column(Numeric)
    unitsinstock = Column(Integer)
    unitsonorder = Column(Integer)
    reorderlevel = Column(Integer)
    discontinued = Column(String)

    order_details = relationship("OrderDetail", back_populates="product")

class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}
    
    employeeid = Column(Integer, primary_key=True)
    lastname = Column(String)
    firstname = Column(String)
    title = Column(String)
    titleofcourtesy = Column(String)
    birthdate = Column(DateTime)
    hiredate = Column(DateTime)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postalcode = Column(String)
    country = Column(String)
    homephone = Column(String)
    extension = Column(String)
    reportsto = Column(Integer)
    notes = Column(String)

    orders = relationship("Order", back_populates="employee")

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'northwind'}
    
    customerid = Column(String, primary_key=True)
    companyname = Column(String)
    contactname = Column(String)
    contacttitle = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postalcode = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)