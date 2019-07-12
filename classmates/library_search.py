import csv
import re
import sys

libraryfile = 'library_collection.csv'
option = sys.argv[1:]
newdata = []
if len(option) > 1:
    sys.exit('Too much cmdline')
elif len(option) == 1:
    if option[0] == '-a':
        with open(libraryfile, 'a', newline='') as fin:
            writer = csv.writer(fin)
            print('書名:', end='')
            newdata.append(input())
            print('著者名:', end='')
            newdata.append(input())
            print('著者名（カナ）:', end='')
            newdata.append(input())
            print('出版社:', end='')
            newdata.append(input())
            print('発行年:', end='')
            newdata.append(input())
            print('ISDN-10:', end='')
            newdata.append(input())
            print('保管棚番号:', end='')
            newdata.append(input())
            writer.writerow(newdata)
            sys.exit()
else:
    pass


def print_result(library_data, i):
    print('書名:', end='')
    print(library_data[i][0])
    print('著者名:', end='')
    print(library_data[i][1])
    print('保管棚番号:', end='')
    print(library_data[i][6])
    print('-' * 30)


print('検索方法を選んでください。')
print('書名で検索（1）／著者名で検索（2）:', end='')

search_mode = int(input())
if search_mode == 1:
    print('書名:', end='')
    book_name = input()
elif search_mode == 2:
    print('著者名:', end='')
    author_name = input().lower()
print('-' * 30)
search_flag = False
with open(libraryfile, 'r') as fin:
    library_data = list(csv.reader(fin))
    if search_mode == 1:
        for i in range(len(library_data)):
            if re.search(book_name, library_data[i][0]):
                print_result(library_data, i)
                search_flag = True
    elif search_mode == 2:
        for i in range(len(library_data)):
            if re.search(author_name, str(library_data[i][1]).lower()) or re.search(author_name, library_data[i][2]):
                print_result(library_data, i)
                search_flag = True
    if search_flag == False:
        print('該当する本がありません。')
