import pytest
from products import Product

def test_creating_prod():
    product = Product("Mac air", 1450, 200, True)
    assert product.name == "Mac air"
    assert product.price == 1450
    assert product.quantity == 200

def test_creating_prod_invalid_details():
    with pytest.raises(Exception) as e:
        product = Product("", -1450, 200, True)
    assert str(e.value) == "Invalid product name"

def test_prod_becomes_inactive():
    product = Product("Mac air", 1450, 100, True)
    buy_quantity = 100
    output = product.buy(buy_quantity)
    assert not product.is_active

def test_buy_modifies_quantity():
    product = Product("Mac air", 1450, 200, True)
    buy_quantity = 50
    output = product.buy(buy_quantity)
    assert product.quantity == 150
    assert output == f'You sell {buy_quantity} {product.name}'

def test_buy_too_much():
    product = Product("Mac air", 1450, 200, True)
    buy_quantity = 300
    with pytest.raises(Exception) as e:
        product.buy(buy_quantity)
    assert str(e.value) == f'Insufficient quantity of {product.name}'


pytest.main()
