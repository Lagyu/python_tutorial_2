from abc import ABCMeta, abstractmethod
import datetime
from typing import List
import csv
import re


class AbstractBook(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def get_author_kana(self) -> str:
        pass

    @abstractmethod
    def get_publisher(self) -> str:
        pass

    @abstractmethod
    def get_publish_date(self) -> datetime.date:
        pass

    @abstractmethod
    def get_isbn(self) -> str:
        pass

    @abstractmethod
    def get_shelf_id(self) -> str:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass

    @abstractmethod
    def set_rent_status(self, bool: bool):
        pass


class Book(AbstractBook):
    def __init__(self, name: str, author: str, author_kana: str, publisher: str, publish_date: datetime.date, isbn: str,
                 shelf_id: str):
        self.name = name
        self.author = author
        self.author_kana = author_kana
        self.publisher = publisher
        self.publish_date = publish_date
        self.isbn = isbn
        self.shelf_id = shelf_id
        self.rent_flag = False
        self.reservation_list = []

    def __repr__(self):
        return "<Book object: " + str(
            [self.name, self.author, self.author_kana, self.publisher, self.publish_date, self.isbn,
             self.shelf_id]) + ">\n"

    def get_name(self) -> str:
        return self.name

    def get_author(self) -> str:
        return self.author

    def get_author_kana(self) -> str:
        return self.author_kana

    def get_publisher(self) -> str:
        return self.publisher

    def get_publish_date(self) -> datetime.date:
        return self.publish_date

    def get_isbn(self) -> str:
        return self.isbn

    def get_shelf_id(self) -> str:
        return self.shelf_id

    def get_status(self) -> bool:
        return self.rent_flag

    def set_rent_status(self, flag_bool: bool):
        self.rent_flag = flag_bool
        return self.rent_flag


class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


class AbstractReservation(metaclass=ABCMeta):
    pass


class Reservation(AbstractReservation):
    def __init__(self, book: AbstractBook, user: User):
        self.user = user
        self.book = book


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []  # type: List[AbstractBook]

    def welcome_message(self):
        return self.name + "にようこそ！"

    def add_book(self, new_book: AbstractBook):
        self.books.append(new_book)
        return self.books

    def search(self, **kwargs) -> List[AbstractBook]:  # library.search(name="aaa", author="bbbbbb")
        keywords_categories = kwargs  # kwargs: { name: "aaa", author: "bbbbbb"}
        result = self.books[:]  # type: List[AbstractBook]
        if "name" in kwargs.keys():
            for book in result[:]:  # はまりポイント
                book_name = book.get_name()
                if book_name.find(kwargs["name"]) == -1:
                    result.remove(book)

        if "author" in kwargs.keys():
            for book in result[:]:
                book_author = book.get_author()
                if book_author.find(kwargs["author"]) == -1:
                    result.remove(book)

        if "author_kana" in kwargs.keys():
            for book in result[:]:
                book_author_kana = book.get_author_kana()
                if book_author_kana.find(kwargs["author_kana"]) == -1:
                    result.remove(book)

        if "publisher" in kwargs.keys():
            for book in result[:]:
                book_publisher = book.get_publisher()
                if book_publisher.find(kwargs["publisher"]) == -1:
                    result.remove(book)

        if "publish_date" in kwargs.keys():
            for book in result[:]:
                book_publish_date = book.get_publish_date()
                if book_publish_date != kwargs["publish_date"]:
                    result.remove(book)

        if "publish_month" in kwargs.keys():
            for book in result[:]:
                book_publish_date = book.get_publish_date()
                if book_publish_date.year != kwargs["publish_month"].year or book_publish_date.month != kwargs[
                    "publish_month"].month:
                    result.remove(book)

        if "publish_year" in kwargs.keys():
            for book in result[:]:
                book_publish_date = book.get_publish_date()
                if book_publish_date.year != kwargs["publish_year"].year:
                    result.remove(book)

        if "isbn" in kwargs.keys():
            for book in result[:]:
                book_isbn = book.get_isbn()
                if book_isbn.find(kwargs["isbn"]) == -1:
                    result.remove(book)

        if "shelf_id" in kwargs.keys():
            for book in result[:]:
                book_shelf_id = book.get_shelf_id()
                if book_shelf_id.find(kwargs["shelf_id"]) == -1:
                    result.remove(book)

        return result


if __name__ == "__main__":

    toshokan = Library("森の図書館")
    with open('book.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            temp_list = row[4].split("/")
            date_list = [int(i) for i in temp_list]
            while len(date_list) < 3:
                date_list.append(1)
            new_book = Book(name=row[0], author=row[1], author_kana=row[2], publisher=row[3],
                            publish_date=datetime.date(date_list[0], date_list[1], date_list[2]), isbn=row[5],
                            shelf_id=row[6])
            toshokan.add_book(new_book)
    while True:
        while True:
            print("検索しましょう。検索項目を選んでください（複数選択可）")
            search_mode = input(
                "1: 書名で検索, 2: 著者名で検索（漢字), 3: 著者名（カナ）で検索, 4: 「出版社」で検索, 5:「発行年」で検索, 6: 「ISBN-10」で検索, 7: 「保管棚番号」）")
            if re.search(r"[1-7]+", search_mode):
                search_query = {}
                if search_mode.find("1") != -1:
                    keyword = input("書名（を含む）：")
                    search_query["name"] = keyword

                if search_mode.find("2") != -1:
                    keyword = input("著者名（を含む）：")
                    search_query["author"] = keyword

                if search_mode.find("3") != -1:
                    keyword = input("著者名(カナ)（を含む）：")

                    search_query["author"] = keyword

                if search_mode.find("4") != -1:
                    keyword = input("出版社（を含む）：")
                    search_query["publisher"] = keyword

                if search_mode.find("5") != -1:
                    while True:
                        keyword = input("出版年（yyyyまたはyyyy/mmまたはyyyy/mm/dd）")
                        if re.search("^\d{4}$", keyword):
                            search_query["publish_year"] = datetime.date(int(keyword), 1, 1)
                            break

                        elif re.search("^\d{4}/\d{1,2}$", keyword):
                            keyword_list = keyword.split("/")
                            search_query["publish_year"] = datetime.date(int(keyword_list[0]), int(keyword_list[1]), 1)
                            break

                        elif re.search("^\d{4}/\d{1,2}/\d{1,2}$", keyword):
                            keyword_list = keyword.split("/")
                            search_query["publish_year"] = datetime.date(int(keyword_list[0]), int(keyword_list[1]),
                                                                         int(keyword_list[2]))
                            break

                        print("入力が不正です。")

                if search_mode.find("6") != -1:
                    keyword = input("ISBN(完全一致)：")
                    search_query["isbn"] = keyword

                if search_mode.find("7") != -1:
                    keyword = input("保管棚番号で検索：")
                    search_query["shelf_id"] = keyword

                if len(search_query) > 0:
                    search_result = toshokan.search(**search_query)
                    break

            else:
                print("1～7の数字を入力してください")

        for i in range(len(search_result)):
            print(i, search_result[i])
        if len(search_result) > 0:
            print(len(search_result), "冊の結果が見つかりました。")
            id_to_rent = int(input("番号を指定して借りる："))
            if search_result[id_to_rent].get_status():
                rent_y_n = input("すでに借りられています。予約しますか？(y/N)")
                if rent_y_n == "Y" or "y":
                    reservation = Reservation(search_result[id_to_rent], User("piyo", 12345))
                else:
                    continue
            else:
                search_result[id_to_rent].set_rent_status(True)
                print(search_result[id_to_rent].get_name(), "を借りました。")
