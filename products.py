"""This file is list the products and make an order, return the amount of order and stock in warehouse"""

class Product:

    def __init__(self, name, price, quantity, is_active=True):
        self.name: str = name
        self.price: float = price
        self.quantity: float = quantity
        # --> this is the total quantity of each item
        self.is_active: bool = is_active
        self.total_quantity = 0

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity: float):
        if quantity == 0:
            self.is_active = False
        return self.is_active

    def show(self):
        return f"{self.name.upper()} |  \tPrice: ${self.price}, \tQuantity: {self.quantity} items"

    def buy(self, quantity):
        price = quantity * self.price
        if quantity <= self.quantity:
            self.quantity -= quantity
        else:
            print('Over stock!')

        return f'$ {price:,d}'
