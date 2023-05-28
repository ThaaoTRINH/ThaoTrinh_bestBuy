import products
import json
from typing import List

file_path = 'product_data.json'

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, maximum=1)
                ]

class Store:
    def __init__(self, products_list):
        self.products_list = products_list

    def list_products(self):
        i = 1
        for product in self.products_list:
            print(f'{i}. {product.show()}')
            i += 1
        print('------------------------------------------------------------------------')

    def get_total_quantity(self):
        total_quantity = 0
        # self.products_list = get_data_json()
        self.products_list = product_list
        for product in self.products_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        for product in self.products_list:
            if product.is_active:
                return self.products_list

    def order(self, shopping_list):
        order_amount = 0
        for product_name, quantity in shopping_list:
            for product in self.products_list:
                if product.name == product_name:
                    print(f'Your ordered: {quantity} {product.name} | {product.promotion}')
                    if product.quantity >= quantity:
                        order_amount += products.Product.amount_promotion(shopping_list, product, quantity)
                        product.quantity -= quantity

        return f'$ {order_amount}'


best_buy = Store(product_list)
