"""This file is list the products and make an order, return the amount of order and stock in warehouse"""
from abc import ABC, abstractmethod
class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent=30):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = product.price * self.percent / 100
        return (product.price - discount) * quantity

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return (product.price * full_price_items) + (product.price / 2 * half_price_items)

class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 3 * 2
        quantity - full_price_items
        return product.price * full_price_items

class Product:

    def __init__(self, name, price, quantity, sell=0, is_active=True):
        if not name:
            raise Exception("Invalid product name")
        if price < 0:
            raise Exception("Invalid product price")
        self.name: str = name
        self.price: float = price
        self.quantity: float = quantity
        self.sell = sell
        self.promotion = None
        self.is_active: bool = is_active
        self.total_quantity = 0

    def set_promotion(self):
        if self.name.upper() == 'MacBook Air M2'.upper():
            self.promotion = 'Second Half price!'
        elif self.name.upper() == 'Bose QuietComfort Earbuds'.upper():
            self.promotion = 'Third One Free!'
        elif self.name == 'Windows License':
            self.promotion = '30% off!'
        else:
            self.promotion = 'None'

        return self.promotion

    def amount_promotion(self, product, quantity):
        if product.name.upper() == 'MacBook Air M2'.upper():
            promotion = SecondHalfPrice(product.name)
            price = promotion.apply_promotion(product, quantity)
        elif product.name.upper() == 'Bose QuietComfort Earbuds'.upper():
            promotion = ThirdOneFree(product.name)
            price = promotion.apply_promotion(product, quantity)
        elif product.name.upper() == 'Windows License'.upper():
            promotion = PercentDiscount(product.name)
            price = promotion.apply_promotion(product, quantity)
        else:
            price = product.price * quantity

        return price + 10

    def remove_promotion(self):
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity: float):
        if quantity == 0:
            self.is_active = False
        return self.is_active

    def show(self):
        promotion_detail = self.set_promotion()
        return f"{self.name.upper()} |  \tPrice: ${self.price}, \tQuantity: {self.quantity} items," \
               f" Promotion: {promotion_detail}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception(f'Insufficient quantity of {self.name}')
        self.quantity -= quantity
        if self.quantity == 0:
            self.is_active = False
        return f'You sell {quantity} {self.name}'

class NonStockedProduct(Product, ABC):
    def __init__(self, name, price, quantity=0):
        super().__init__(name=name, price=price, quantity=quantity)

    def show(self):
        return f"{self.name.upper()} |  \tPrice: ${self.price}, \tQuantity: Unlimited, Promotion: 30% off"

class LimitedProduct(Product, ABC):
    def __init__(self, name, price, quantity=1, maximum=1):
        super().__init__(name=name, price=price, quantity=quantity)
        self.maximum = maximum

    def show(self):
        return f"{self.name.upper()} |  \tPrice: ${self.price}, \tLimited to 1 per order!, \t Promotion: None"
