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


cook_book = {}

def read_course(f):
  course_name = f.readline()
  print(course_name)
  ing_count = int(f.readline())
  
  for i in range(ing_count):
    line = f.readline()
    list_line = line.split("|")
    print(list_line)
  

with open('file11.txt', encoding ='utf-8') as file1:
  while True:
    read_course(file1)
    empty_line = file1.readline()
    if empty_line == '':
      break

print("Cook book:")
print(cook_book)
    


  

    







  


     