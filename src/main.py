from controllers.generate_order import generate_order
from controllers.generate_order_orm import generate_order_orm
from controllers.generate_data import generate_order_data
from controllers.generate_data import generate_employees_data

def app():
    while True:
        print("\nOpções:")
        print("1. Gerar um novo pedido (driver)")
        print("2. Gerar um novo pedido (ORM)")
        print("3. Relatório de informações completas sobre um pedido")
        print("4. Relatório de ranking dos funcionários por intervalo de tempo")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            customer_id = input('Customer ID: ')
            product_id = int(input('Product ID: '))
            quantity = int(input('Quantity: '))
            employee_id = int(input('Employee ID: '))

            try:
                generate_order(product_id, customer_id, quantity, employee_id)
            except BaseException as e:
                print(e)

        elif choice == "2":
            customer_id = input('Customer ID: ')
            product_id = int(input('Product ID: '))
            quantity = int(input('Quantity: '))
            employee_id = int(input('Employee ID: '))
            try:
                generate_order_orm(product_id, customer_id, quantity, employee_id)
            except BaseException as e:
                print(e)

        elif choice == "3":
            order_id = int(input('Order ID: '))
            try:
                order = generate_order_data(order_id)
                for (key, value) in order:
                    if (key.startswith('_')):
                        continue
                    
                    print(f"{key}: {value}")
            except BaseException as e:
                print(e)
            pass
        
        elif choice == "4":
            start_date = input('Start date (YYYY-MM-DD): ')
            end_date = input('End date (YYYY-MM-DD): ')
            ranking = generate_employees_data(start_date, end_date)
            for record in ranking:
                print(f'Employee: {record.firstname} {record.lastname}, Total Orders: {record.total_orders}, Total Sales: {record.total_sales}')
        
        elif choice == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == '__main__':
    app()
