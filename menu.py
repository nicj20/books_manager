import os
import helpers
import manager as mg


def start():
    while True:
        helpers.clean_screen()

        print("======================")
        print("Welcome to your Books Manager")
        print("======================")
        print("[1] Books List    ")
        print("[2] Search Book   ")
        print("[3] Add Book     ")
        print("[4] Modify Book   ")
        print("[5] Delete Book   ")
        print("[6] Close Manager   ")
        print("======================")

        option = input('<')
        helpers.clean_screen()

        if option == '1':
            print("Books List ==> \n")
            for book in mg.Books.books_list:
                print(book)

        if option == '2':
            print("Search Book ==> \n")
            u_book = helpers.read(1, 30, "Name=> ").upper()
            book = mg.Books.search_book(u_book)
            print(book) if book else print("The client haven't been found")

        if option == '3':
            print("Add Book ==> \n")

            name = None
            while True:
                name = helpers.read(1, 30, "Name").upper()
                if helpers.valid_book(name, mg.Books.books_list):
                    break
            score = float(helpers.read(1, 2, "Score(1-10)"))
            author = helpers.read(2, 30, "Author").upper()
            mg.Books.add_book(score, name, author)

        if option == '4':
            print("Modify Book ==> \n")
            name = helpers.read(1, 30, "Name").upper()
            client = mg.Books.search_book(name)
            if book:
                score = float(helpers.read(
                    1, 1, f"Score=> [{book.score}]"))
                author = helpers.read(
                    2, 30, f"Author => [{book.author}]").capitalize()
                mg.Books.modify_book(score, name, author)
                print("Successfully modified")
            else:
                print("Movie not found")

        if option == '5':
            print("Delete Book ==> \n")
            name = helpers.read(1, 30, "Name").upper()
            print("Successfully deleted") if mg.Books.delete_book(name) else print("Movie not found")

        if option == '6':
            print("Closing ==> \n")
            break

        input("Press ENTER to choose another option")


