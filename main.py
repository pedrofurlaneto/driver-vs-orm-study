from models.dao.costumers_dao import get_costumer_by_id

costumer_id = input('costumerid: ')
costumer = get_costumer_by_id(costumer_id.upper())

if costumer is None:
    print('Usuario nao encontrado')
    

# product_id = int(input('productid: '))
# quantity = int(input('quantity: '))

# units_in_stock = get_product_units_in_stock(product_id)

# print('units_in_stock - quantity', units_in_stock - quantity)

# if units_in_stock - quantity < 0:
#     print('Produto indisponível')
    