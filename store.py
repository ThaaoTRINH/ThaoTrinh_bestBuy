import products
import json
from typing import List

file_path = 'product_data.json'

class Store:
    def __init__(self, products_list):
        self.products_list = products_list

    def save_to_json(self):
        my_list = []
        for product in self.products_list:
            product_dict = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'status': True
            }
            my_list.append(product_dict)

            with open(file_path, 'w') as file:
                json.dump(my_list, file)

    def list_products(self):
        i = 1
        for product in self.products_list:
            print(f'{i}. {product.show()}')
            i += 1
        print('------------------------------------------------------------------------')

    def add_product(self):
        print('INPUT PRODUCT TO WAREHOUSE')
        product_name = input('Product name: > ')
        product_price = float(input('Product price: > '))
        product_quantity = int(input('Quantity of product: > '))

        new_product_object = products.Product(product_name, product_price, product_quantity, True)

        product_exists = False
        for product in self.products_list:
            if product.name == product_name:
                product.quantity += product_quantity
                product_exists = True

        if not product_exists:
            products_list.append(new_product_object)
        self.save_to_json()
        return self.products_list

    def remove_product(self, product_name):
        self.products_list = get_data_json()

        for product in self.products_list:
            if product_name == product.name:
                self.products_list.remove(product)
        self.save_to_json()
        return self.products_list

    def update_product(self):
        product_number = int(input('Enter product # need to update: > '))
        product_price = float(input('Enter new price > '))
        self.products_list = get_data_json()

        product_name_list = []
        for product in self.products_list:
            product_name_list.append(product.name)

        for product in self.products_list:
            if product_name_list[product_number - 1] == product.name:
                product.price = product_price
        self.save_to_json()
        return self.products_list

    def search_product(self):
        self.products_list = get_data_json()
        while True:
            button = input('Name / Price / Quantity. Which one you want to search: > ')
            if button.lower() == 'name':
                while True:
                    name = input('Enter name to search: ')
                    for product in self.products_list:
                        if name.upper() == product.name:
                            print(product.show())
                    print('------------------------------------------------------------------------')
                    break
            elif button.lower() == 'price':
                while True:
                    max_price = float(input('Enter the maximum price: >'))
                    min_price = float(input('Enter the minimum price: >'))
                    print('--------------------------------------------------------')
                    print(f'PRODUCTS PRICE BETWEEN ${min_price} and ${max_price} : ')
                    for product in self.products_list:
                        if (product.price <= max_price) and (product.price >= min_price):
                            print(f'Product: {product.name } | Price: {product.price }')
                    print('------------------------------------------------------------------------')
                    break
            elif button.lower() == 'quantity':
                while True:
                    quantity_search = int(input('Enter quantity number: >'))
                    print('------------------------------------------------------------------------')
                    print(f'PRODUCT WHICH HAS BELOW {quantity_search} QUANTITY')
                    for product in self.products_list:
                        if product.quantity <= quantity_search:
                            print(f'Product: {product.name } | Quantity: {product.quantity }')
                    print('------------------------------------------------------------------------')
                    break
            break

    def sort_product(self):
        self.products_list = get_data_json()
        print('------------------------------------------------------------------------')
        print('PRODUCTS LIST SORTED BY QUANTITY')
        sorted_products = sorted(self.products_list, key=lambda x: x.quantity, reverse=True)
        for product in sorted_products:
            print(product.show())
        print('------------------------------------------------------------------------')

    def get_total_quantity(self):
        total_quantity = 0
        self.products_list = get_data_json()
        for product in self.products_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        for product in self.products_list:
            if product.is_active:
                return self.products_list

    def order(self, shopping_list):
        shopping_price = 0
        for product_name, quantity in shopping_list:
            for product in self.products_list:
                if product.name == product_name:
                    if product.quantity >= quantity:
                        shopping_price += product.price * quantity
                        product.quantity -= quantity
                    else:
                        print(f'Stock is not enough for {product.name}')
                    break
        self.save_to_json()
        return f'$ {shopping_price:,.2f}'

def get_data_json():
    product_list = []
    with open(file_path, 'r') as file:
        data = json.loads(file.read())
    for line in data:
        product_info = products.Product(line['name'], line['price'], line['quantity'], line['status'])
        product_list.append(product_info)
    return product_list


products_list = get_data_json()
best_buy = Store(products_list)
