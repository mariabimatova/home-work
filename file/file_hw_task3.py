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


def merge_files(input_files, output_file):
    info = []
    for file in input_files:
        with open(file, encoding='utf-8') as f:
            readfile = f.readlines()
            readfile_len = len(readfile)
            d = {'name': file, 'lines': readfile, 'line_count': readfile_len}
            info.append(d)

    info.sort(key=lambda i: i['line_count'])

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for d in info:
            file = d['name']
            readfile_len = d['line_count']
            readfile = d['lines']
            out_f.write(file)
            out_f.write('\n')
            out_f.write(str(readfile_len))
            out_f.write('\n')
            for i in readfile:
                out_f.write(i)
            out_f.write('\n')


def main():
    input_files = ['file2.txt', 'file3.txt', 'file1.txt']
    output_file = 'out.txt'
    merge_files(input_files, output_file)


main()
