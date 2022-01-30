'''Необходимо объединить их в один по следующим правилам:

Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них 
(то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
Пример Даны файлы: 1.txt

Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
2.txt

Строка номер 1 файла номер 2
Итоговый файл:

2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1'''


file1 = 'file11.txt'
with open(file1, encoding='utf-8') as f11:
    readf11 = f11.readlines()
    readf11len = int(len(readf11))
file2 = 'file2.txt'
with open(file2, encoding='utf-8') as f2:
    readf2 = f2.readlines()
    readf2len = int(len(readf2))
if readf11len >= readf2len:
    with open('join_file1.txt', 'a', encoding='utf-8') as fw2:
        fw2.write(file2)
        fw2.write('\n')
        fw2.write('1')
        fw2.write('\n')
        for i in readf2:
            fw2.write(f'Строка номер {readf2.index(i)+1} {file2}: \n {i}')
        fw2.write(file1)
        fw2.write('\n')
        fw2.write('2')
        fw2.write('\n')
        for i in readf11:
            fw2.write(f'Строка номер {readf11.index(i)+1} {file1}: \n {i}')
else:
    with open('join_file1.txt', 'a', encoding='utf-8') as fw2:
        fw2.write(file1)
        fw2.write('\n')
        fw2.write('1')
        fw2.write('\n')
        for i in readf11:
            fw2.write(f'Строка номер {readf11.index(i)+1} {file1}: \n {i}')
        fw2.write(file2)
        fw2.write('\n')
        fw2.write('2')
        fw2.write('\n')
        for i in readf2:
            fw2.write(f'Строка номер {readf2.index(i)+1} {file2}: \n {i}')
