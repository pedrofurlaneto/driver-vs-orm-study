from connect import connect_database

bd_connection = connect_database()

session = bd_connection.cursor()
products = session.execute("SELECT productid, productname, unitprice, unitsinstock FROM northwind.products WHERE unitprice < 40")
for product in products:
    print(product)
