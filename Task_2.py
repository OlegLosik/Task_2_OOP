import os
def food_list():
    with open ('Receipes.txt', 'r', encoding='utf8') as receipes:
        cook_book = {}
        for line in receipes:
            food_name = line.strip()
            cook_book [food_name] = []
            products_count = receipes.readline()
            for _ in range(int(products_count)):
                prod = receipes.readline()
                ingredient_name, quantity, measure = prod.split('|')
                receipe = {'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure.split()}
                cook_book[food_name].append(receipe)
            receipes.readlines()
        #task_2
        person_count = 2
        shop_list = {}
        for _ in cook_book:
            total = cook_book[food_name]
            for costs in total:
                shop_list_by_dish = costs
                name_product = shop_list_by_dish['ingredient_name']
                weight = shop_list_by_dish['measure']
                amount = int (shop_list_by_dish['quantity']) * person_count
                weight_amount = {'measure' : weight, 'quantity' : amount}
                if name_product not in shop_list:
                    shop_list[name_product] = weight_amount
                else:
                    shop_list[name_product]['quantity'] = shop_list[name_product]['quantity'] + amount
        print (shop_list)
    return
food_list()