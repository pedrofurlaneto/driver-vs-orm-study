from costumers_dao import get_costumer_by_id
from products_dao import get_product_by_id
    
def app():
    costumer_id = input('costumerid: ')
    costumer = get_costumer_by_id(costumer_id)

    print(costumer)

    # if costumer is None:
    #     print('Cliente nao encontrado')

    # product_id = int(input('productid: '))
    # product = get_product_by_id(product_id)
    # print(product)

    # if product is None:
    #     print('Produto não encontrado')
    #     return

    # quantity = int(input('quantity: '))
    
app()