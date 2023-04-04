import csv
import paths


class Create_Book:

    def __init__(self, score, name, author):
        self.score = score
        self.name = name
        self.author = author

    def __str__(self):
        return f"({self.score}),{self.name},{self.author}"


class Books:
    books_list = []

    with open(paths.DATABASE_PATH, newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        for score, name, author in reader:
            book = Create_Book(score, name, author)
            books_list.append(book)

    @staticmethod
    def search_book(name):
        for book in Books.books_list:
            if book.name == name:
                return book

    @staticmethod
    def add_book(score, name, author):
        book = Create_Book(score, name, author)
        Books.books_list.append(book)
        Books.save()
        return book

    @staticmethod
    def modify_book(score, name, author):
        for base, book in enumerate(Books.books_list):
            if book.name == name:
                Books.books_list[base].score = score
                Books.books_list[base].author = author
                Books.save()
                return Books.books_list[base]

    @staticmethod
    def delete_book(name):
        for i, book in enumerate(Books.books_list):
            if book.name == name:
                book_ = Books.books_list.pop(i)
                Books.save()
                return book_

    @staticmethod
    def save():
        with open(paths.DATABASE_PATH, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for book in Books.books_list:
                writer.writerow((book.score, book.name, book.author))
