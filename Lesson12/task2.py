'''
Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class

Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

'''


class Author:

    def __init__(self, name: str, country='', birthday=(), books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self._books = books

    def __str__(self):
        return f'\nAuthor: {self.name},\nBorn: {self.birthday},\nCountry: {self.country}'

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, value):
        self._books = value

    def __repr__(self):
        return self.__str__()


class Book:

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'\nBook: {self.name} year: {self.year}{self.author}'

    def __repr__(self):
        return f'{self.name} year: {self.year}'


class Library:
    books_amount = 0

    def __init__(self, name: str, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = set(authors)
        self.books_amount += 1

    def new_book(self, name: str, year: int, author: Author):
        if isinstance(author, str):
            author = Author(author)

        if not name in author.books:
            author.books.append(name)
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.authors.add(author)
        return new_book

    def authors_books(self, author: Author):
        return list(filter(lambda book: book.author.name == author.name, self.books))

    def group_by_author(self):
        dict_group_by_author = {}
        for author in self.authors:
            dict_group_by_author[author.name] = self.authors_books(author)
        return dict_group_by_author

    def group_by_year(self, year: int):
        return list(filter(lambda book: book.year == year, self.books))

    def __str__(self):
        books_by_author = self.group_by_author()
        authors_books_str = [author + '\n\t' + '\n\t'.join(map(repr, books))
                    for author, books in books_by_author.items()]
        template = '\n'.join(authors_books_str)
        return f"{self.name}:\n{template}"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    author1 = Author('Boris Akunin', 'Russia', (1956, 5, 20))
    author2 = Author('Sir Terence David John Pratchett',
                     'England', (1948, 4, 28))
    library = Library('Central Library')
    library.new_book('The Turkish Gambit', 1998, author1)
    library.new_book('The Jack of Spades', 1999, author1)
    library.new_book('Just Masa', 2020, author1)
    library.new_book('Good Omens', 1990, author2)
    library.new_book('Going Postal', 2004, author2)
    library.new_book('Leviathan', 1998, author1)
    library.new_book('Hogfather', 1996, author2)
    library.new_book('The Lord of the Rings', 1955,
                     'John Ronald Reuel Tolkien')
    print(library.authors_books(author2))
    print(library.group_by_year(1990))
    print(library)
