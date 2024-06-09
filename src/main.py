from controllers.generate_order import generate_order

def app():
    customer_id = input('customerid: ')
    product_id = int(input('productid: '))
    quantity = int(input('quantity: '))
    employee_id = int(input('employeeid: '))

    try:
        generate_order(product_id, customer_id, quantity, employee_id)
    except BaseException as e:
        print(e)

if __name__ == '__main__':
    app()