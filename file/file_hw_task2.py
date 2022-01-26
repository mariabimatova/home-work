'''
Задание 2.
Нужно написать функцию, которая на вход принимает
 список блюд из cook_book и количество персон для кого мы будем готовить

get_shop_list_by_dishes(dishes, person_count)

На выходе мы должны получить словарь 
с названием ингредиентов и его количества для блюда. Например, для такого вызова

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

Должен быть следующий результат:

{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}

'''

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Яйцо', 'quantity': 5, 'measure': 'шт.'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    r = {}
    for course in dishes:
        ingredients = cook_book[course]
        for ing in ingredients:
            ing_name = ing['ingredient_name']
            if ing_name not in r:
                d = {}
                d['measure'] = ing['measure']
                d['quantity'] = ing['quantity']*person_count
                r[ing_name] = d
            else:
                d['quantity'] = d['quantity'] + ing['quantity']*person_count

    return r


d = ['Запеченный картофель', 'Омлет']
result = get_shop_list_by_dishes(d, 2)
print(result)
