'''cook_book = {
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
    ]'''


def read_course(f, cook_book):
    course_name = f.readline().strip()
    ing_count = int(f.readline())
    m = []
    cook_book[course_name] = m

    for i in range(ing_count):
        line = f.readline().strip()
        list_line = line.split("|")
        ing_dict = {}
        ing_dict["ingredient_name"] = list_line[0].strip()
        ing_dict["quantity"] = int(list_line[1])
        ing_dict["measure"] = list_line[2].strip()
        m.append(ing_dict)


def load_cook_book_from_file(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file1:
        while True:
            read_course(file1, cook_book)
            empty_line = file1.readline()
            if empty_line == '':
                break
    print("Cook book:")
    print(cook_book)


load_cook_book_from_file('file11.txt')
