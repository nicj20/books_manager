import re
import os
import platform


def clean_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def read(length_min=1, length_max=100, message=None):
    print(message) if message else None
    while True:
        text = input('> ')
        if length_min <= len(text) <= length_max:
            return text


def valid_book(name, b_list):

    for book in b_list:
        if book.name == name:
            print('This ID is already in he system')
            return False

    return True
