from pickle import NONE
import unittest
import manager as mg
import copy
import paths
import csv

class Test_database(unittest.TestCase):

    def setUp(self):
        mg.Books.books_list = [
            mg.Create_Book('10', 'Harry Potter', 'J.K Rowling'),
            mg.Create_Book('7', 'Ducks', 'Kate Beaton'),
            mg.Create_Book('6', 'Tokyo Blues', 'Haruki Murakami')
        ]
    
    def test_search_book(self):
        book = mg.Books.search_book('Harry Potter')
        no_book = mg.Books.search_book('The little prince')
        self.assertIsNotNone(book)
        self.assertIsNone(no_book)

    def test_add_book(self):
        book = mg.Books.add_book('5', 'Never Never', 'Collen Hoover')
        self.assertEqual(len(mg.Books.books_list), 4)
        self.assertEqual(book.score, '5')
        self.assertEqual(book.name, 'Never Never')
        self.assertEqual(book.author, 'Collen Hoover')

    def test_modify_client(self):
        book_modify = copy.copy(mg.Books.search_book('Tokyo Blues'))
        new_book = mg.Books.modify_book('4', 'Tokyo Blues', 'James Clear')
        self.assertEqual(book_modify.score, '6')
        self.assertEqual(new_book.score, '4')

    def test_delete_client(self):
        book_deleted = mg.Books.delete_book('Ducks')
        book = mg.Books.search_book('Ducks')
        self.assertEqual(book_deleted.name, 'Ducks')
        self.assertIsNone(book)
    
    def save_test(self):
        mg.Books.delete_book('Tokyo Blues')
        mg.Books.delete_book('Atomic Habits')
        mg.Books.modify_book('7', 'Harry Potter', 'J.K Rowling')

        name, score, author = None, None, None
        with open(paths.DATABASE_PATH, newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            name, score, author = next(reader)

        self.assertEqual(score, '7')
        self.assertEqual(name, 'Harry Potter')
        self.assertEqual(author, 'J.K Rowling')



if __name__=="__main__":
    unittest.main()
