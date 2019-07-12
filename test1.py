import re
from typing import Pattern, List

from abc import ABCMeta, abstractmethod


def main():
    book_store = BookStore(Categories(), Authors())
    while True:
        print("""
1. 書籍の登録
2. 書籍の表示
3. 書籍データをファイルに保存
4. 書籍データをファイルから読み込む
9. 終了
""")
        # 書籍データの形式
        # {name: "name_str", author: "author_str"}
        menu = int(input("番号を入力してください : "))
        if menu == 1:
            # 書籍の登録
            name_str = input("書名を入力してください。")
            author_str = input("著者名を入力してください。")
            category_str = input("著者名を入力してください。")

            author = Author(name=author_str)
            # book = Book(name=name_str, author=Author.))

        elif menu == 2:
            # 書籍の表示
            pass
        elif menu == 3:
            # 書籍データをファイルに保存
            pass
        elif menu == 4:
            # 書籍データをファイルから読み込む
            pass
        else:
            print("ご利用ありがとうございました。")
            break


class AbstractObjects(metaclass=ABCMeta):
    def __init__(self, keys_str_list: list, parent_class):
        self.keys_str_list = keys_str_list
        self.obj_list = []
        self.parent_class = parent_class

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def filter(self, **kwargs):
        pass

    @abstractmethod
    def get_or_create(self, **kwargs):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def all(self, **kwargs):
        pass


class Objects(AbstractObjects):
    def __init__(self, keys_str_list: list, parent_class):
        super().__init__(keys_str_list, parent_class)

    def key_check(self, kw_keys_list):
        """
        Checks if key is valid.
        :param kw_keys_list:
        :return:
        """
        for key in  kw_keys_list:
            if key not in self.keys_str_list:
                raise KeyError("No such key: "+ key)
        return

    def all(self) -> list:
        return self.obj_list

    def filter(self, **kwargs) -> list:
        """

        :param kwargs:
        :return:
        """
        keys = list(kwargs.keys())
        result_candidates = self.obj_list

        self.key_check(keys)

        for key in keys:
            search_reg_exp = re.compile(kwargs.get(key))
            result_candidates = [obj for obj in result_candidates if bool(search_reg_exp.search(obj.key))]

        return result_candidates

    def get(self, **kwargs):
        """
        :param kwargs: RegExp str to search.
        :return: one object.
        """

        result = self.filter(**kwargs)
        length_of_result = len(result)
        if length_of_result == 0:
            return None
        elif length_of_result == 1:
            return result[0]
        else:
            print("Too many results:", result)
            print("Returned the first object:", result[0])
            return result[0]

    def get_or_create(self, **kwargs):
        get_result = self.get(**kwargs)
        if get_result is None:
            created = self.__create(**kwargs)

        return created

    def __create(self, **kwargs):
        """
        Use this after checks.
        :param kwargs:
        :return:
        """
        created = self.parent_class(**kwargs)
        self.obj_list.append(created)
        return created

    def create(self, **kwargs):
        get_result = self.get(**kwargs)
        if get_result is None:
            return self.__create(**kwargs)
        else:
            raise ValueError("The value you tried to create already exists.")


class AbstractObject(metaclass=ABCMeta):
    def __init__(self):
        self.objects = AbstractObjects()


class AbstractAuthor(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.name = None

    def __str__(self) -> str:
        pass


class Author(AbstractAuthor):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.objects = AbstractAuthors()

    def __str__(self) -> str:
        return self.name


class AbstractAuthors(metaclass=ABCMeta, AbstractObjects):
    @abstractmethod
    def add_author(self, author: AbstractAuthor) -> bool:
        pass


class Authors(AbstractAuthor):
    def __init__(self, name: str):
        super().__init__(name)
        self.authors = []

    def add_author(self, author: AbstractAuthor):
        author_name_str_list = [elm.name for elm in self.authors]
        if author.name in author_name_str_list:
            return author
        else:
            self.authors.append(author)
            return author


class AbstractCategory(metaclass=ABCMeta):
    def __init__(self, name, category_number_str, root_categories):
        self.name = None
        self.category_number_str = None

    @abstractmethod
    def __str__(self) -> str:
        pass


class AbstractCategories(metaclass=ABCMeta):
    def __init__(self):
        self.categories = None

    @abstractmethod
    def search_by_name(self, query_regexp: Pattern, mode="forward_match") -> List:
        pass

    @abstractmethod
    def search_by_category_number(self, query_regexp: Pattern) -> List:
        pass

    @abstractmethod
    def add_category(self, category: AbstractCategory):
        pass


class Categories(AbstractCategories):
    def __init__(self):
        super().__init__()
        self.categories = []

    def search_by_name(self, query_regexp: Pattern, mode="forward_match"):
        result_list = []
        for category in self.categories:
            if query_regexp.match(category.name):
                result_list.append(category)
        return result_list

    def search_by_category_number(self, query_regexp: Pattern):
        result_list = []
        for category in self.categories:
            if query_regexp.match(category.name):
                result_list.append(category)
        return result_list

    def add_category(self, category: AbstractCategory):
        category_number_str_list = [str(category_item) for category_item in self.categories]
        if category.category_number_str in category_number_str_list:
            return self
        else:
            self.categories.append(category)
            return self


class Category(AbstractCategory):
    def __init__(self, name: str, category_number_str: str, root_categories: Categories):
        super().__init__(name, category_number_str, root_categories)
        self.name = name
        self.category_number_str = category_number_str
        root_categories.add_category(self)

    def __str__(self) -> str:
        return self.category_number_str


class AbstractBook(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name: str, author: Author, category: Category):
        pass


class Book(AbstractBook):
    def __init__(self, name: str, author: Author, category: Category):
        super().__init__(name, author, category)
        self.name = name
        self.author = author
        self.category = category


class BookStore:
    def __init__(self, categories: AbstractCategories, authros: Authors):
        self.categories = categories
        self.authors = authros
        self.store = []

    def get_categories(self):
        return self.categories

    def register_book(self, book: AbstractBook):
        self.store.append(book)
        return self.store
