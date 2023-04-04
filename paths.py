import sys

DATABASE_PATH = "books.csv"

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'books_test.csv'
