import store

menu = """1. List all products in store        
2. Show total items in store
3. Make an order                                           
4. Quit"""

def make_order():
    products_list = store.product_list
    print('------------------------------------------------------------------------')
    i = 1
    product_name_list = []
    for product in products_list:
        product_name_list.append(product.name)
        print(f'{i}. {product.show()}')
        i += 1
    print('------------------------------------------------------------------------')
    print('When you want to finish order, enter empty text.')
    order_list = []

    while True:
        product_number = input('Which product # do you want? ')
        if product_number == '':
            break
        if product_name_list[int(product_number) - 1].upper() == 'SHIPPING':
            print('Invalid! ')
            break
        if product_name_list[int(product_number) - 1].upper() == 'WINDOWS LICENSE':
            product_amount = 1
            print('Just 1 "WINDOWS LICENSE" for each order')
            break
        product_amount = input("What amount do you want? ")
        if product_number != '' and product_amount != '':
            print('Product added to list!')
            print()

            order_list.append((product_name_list[int(product_number) - 1], int(product_amount)))
        else:
            break
    return order_list

def main():
    print('------------------------------------------------------------------------')
    print('                             STORE MENU')
    print('------------------------------------------------------------------------')

    while True:
        print(menu)
        number = int(input('Please choose a number: '))
        print()

        if number == 4:
            print('Thank you')
            break
        if number == 1:
            print('LIST PRODUCTS IN STORE')
            store.Store.list_products(store.best_buy)
        elif number == 2:

            total_item = store.Store.get_total_quantity(store.best_buy)
            print('------------------------------------------------------------------------')
            print(f'Total of {total_item} items in store')
            print('------------------------------------------------------------------------')
        elif number == 3:
            order_list = make_order()
            print('------------------------------------------------------------------------')
            print(f'Order made! Total payment is: {store.Store.order(store.best_buy, order_list)}')
            print('(Include $10 shipping fee)')
            print('------------------------------------------------------------------------')

        else:
            print('Invalid number. Try again! ')


if __name__ == '__main__':
    main()
