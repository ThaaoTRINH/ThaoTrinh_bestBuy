import store

menu = """1. List all products in store         2. Show total items in store
3. Make an order                      4. Add product into warehouse
5. Remove product from warehouse      6. Update for product
7. Search product (Name / Price / Quantity)
8. Sort products                      9. Quit"""

def make_order():
    products_list = store.get_data_json()
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

        if number == 9:
            print('Thank you')
            break
        if number == 1:
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
            print('------------------------------------------------------------------------')

        elif number == 4:
            store.Store.add_product(store.best_buy)
            store.Store.list_products(store.best_buy)

        elif number == 5:
            product_name = input('Enter the name of product to remove: > ')
            store.Store.remove_product(store.best_buy, product_name)
            store.Store.list_products(store.best_buy)
        elif number == 6:
            store.Store.update_product(store.best_buy)
            store.Store.list_products(store.best_buy)
        elif number == 7:
            store.Store.search_product(store.best_buy)
        elif number == 8:

            store.Store.sort_product(store.best_buy)
        else:
            print('Invalid number. Try again! ')


if __name__ == '__main__':
    main()
