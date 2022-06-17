from pprint import pprint

name = 'reciples.txt'


def recipe_list(name):
    cook_book = {}

    with open(name, 'r', encoding='utf-8') as file:

        for line in file:
            food_name = line.strip()
            ingredients = []

            for item in range(int(file.readline())):
                all_ingredient = {}
                ingredient = file.readline().strip()
                all_ingredient['ingredient_name'], all_ingredient['quantity'], all_ingredient['measure'] = ingredient.split('|')
                all_ingredient['quantity'] = int(all_ingredient['quantity'])

                ingredients.append(all_ingredient)
            file.readline()
            cook_book[food_name] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person):
    ingredients_list = {}
    for dish in dishes:
        for ingredient in recipe_list(name)[dish]:
            name_ingredient = ingredient.pop('ingredient_name')
            ingredient['quantity'] = int(ingredient['quantity']) * int(person)
            if name_ingredient in ingredients_list:
                ingredient['quantity'] += ingredients_list[name_ingredient]['quantity']
            ingredients_list.update({name_ingredient: ingredient})
    return ingredients_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
