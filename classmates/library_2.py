import csv
import sys


def search():
    print("こちらは書籍検索システムです")
    kensaku = input('検索ワードを入力してください:')

    try:

        with open("book.csv", "r", encoding="utf-8") as f:
            data = csv.reader(f)
            j = 0
            for n in data:
                a = ','.join(n)

                if kensaku in a:
                    j += 1
                    print("\n{0:d}件目".format(j))
                    print("書名：{0:s}".format(n[0]))
                    print("著者名：{0:s}".format(n[1]))
                    print("著者名（カナ）：{0:s}".format(n[2]))
                    print("出版社：{0:s}".format(n[3]))
                    print("発行年：{0:s}".format(n[4]))
                    print("ISBN-10：{0:s}".format(n[5]))
                    print("保管棚番号：{0:s}".format(n[6]))
                    # print("\n")
                else:
                    # print("該当するものが見つかりませんでした")
                    pass

    except KeyboardInterrupt:
        sys.exit()


def addbook():
    print("新しい書籍を追加します")
    with open("book.csv", "a") as f:
        bname1 = input("書名を入力してください:")
        f.write(bname1 + ",")

        bname2 = input("著者名を入力してください:")
        f.write(bname2 + ",")

        bname3 = input("著者名（カナ）を入力してください:")
        f.write(bname3 + ",")

        bname4 = input("出版社を入力してください:")
        f.write(bname4 + ",")

        bname5 = input("発行年を入力してください:")
        f.write(bname5 + ",")

        bname6 = input("ISBN-10を入力してください:")
        f.write(bname6 + ",")

        bname7 = input("保管棚番号を入力してください:")
        f.write(bname7 + "\n")

        print("\n以上の内容でよろしいですか？")
        print("書名:", bname1)
        print("著者名:", bname2)
        print("著者名（カナ）:", bname3)
        print("出版社:", bname4)
        print("発行年:", bname5)
        print("ISBN-10:", bname6)
        print("保管棚番号:", bname7)

        answer = input("(y/n):")
        if answer == "y":
            print("書籍が追加されました")
            sys.exit()
        elif answer == "n":
            pass


select = input("a:書籍検索 b:書籍追加 (a/b):")

if select == "a":
    search()
elif select == "b":
    addbook()
else:
    print("ご利用ありがとうございました")
    sys.exit()

