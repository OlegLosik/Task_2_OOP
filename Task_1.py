def cook_book():
    with open("Receipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split("\n\n"):
            name, _, *products = line.split("\n")
            cook_list = []
            for prod in products:
                ingredient_name, quantity, measure = map(
                    lambda x: int(x) if x.isdigit() else x, prod.split(" | ")
                )
                cook_list.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": quantity,
                        "measure": measure,
                    }
                )
            cook_book[name] = cook_list
    return cook_book

print(cook_book())