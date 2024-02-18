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
            receipes.readline()
            print(cook_book)
    return
food_list()