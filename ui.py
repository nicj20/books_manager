import helpers
import manager as mg
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixing:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)
        self.geometry(f"{w}x{h}+{x}+{y}")


class Create_Book_Window(Toplevel, CenterWidgetMixing):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create Book")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        Label(frame, text="Name").grid(row=0, column=0)
        Label(frame, text="Score").grid(row=0, column=1)
        Label(frame, text="Author").grid(row=0, column=2)

        name = Entry(frame)
        name.grid(row=1, column=0)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        score = Entry(frame)
        score.grid(row=1, column=1)
        score.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        author = Entry(frame)
        author.grid(row=1, column=2)
        author.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        create = Button(frame, text="Create", command=self.create_book) #change command
        create.configure(state=DISABLED)
        create.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [0, 0, 0]
        self.create = create  # Create(BUTTON)
        self.name = name
        self.score = score
        self.author = author

    def create_book(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.name.get(),
            values=(int(self.score.get()), self.name.get().upper(), self.author.get().upper()))
        mg.Books.add_book(int(self.score.get()), self.name.get().upper(), self.author.get().upper())
        self.close()

    def close(self):
        self.destroy()
        self.update

    def validate(self, event, index):
        valid = False
        value = event.widget.get()
        if index == 0:
            valid = helpers.valid_book(value, mg.Books.books_list)
            if valid:
                event.widget.configure({"bg": "Green"})
            else:
                event.widget.configure({"bg": "Red"})

        if index == 1:
            try:
                valid = int(value) in list(range(1, 11))
                if valid:
                    event.widget.configure({"bg": "Green"})
                else:
                    event.widget.configure({"bg": "Red"})
            except ValueError:
                event.widget.configure({"bg": "Red"})

        if index == 2:
            valid = 2 <= len(value) <= 30
            if valid:
                event.widget.configure({"bg": "Green"})
            else:
                event.widget.configure({"bg": "Red"})

        # Change the button state
        self.validations[index] = valid
        self.create.config(state=NORMAL if self.validations == [1, 1, 1] else DISABLED)


class Modify_Book_Window(Toplevel, CenterWidgetMixing):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modify Client")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        Label(frame, text="Name").grid(row=0, column=1)
        Label(frame, text="Score").grid(row=0, column=0)
        Label(frame, text="Author").grid(row=0, column=2)

        score = Entry(frame)
        score.grid(row=1, column=0)
        score.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        author = Entry(frame)
        author.grid(row=1, column=2)
        author.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        book = self.master.treeview.focus()
        spaces = self.master.treeview.item(book, 'values')

        score.insert(0, spaces[0])
        name.insert(0, spaces[1])
        author.insert(0, spaces[2])

        frame = Frame(self)
        frame.pack(pady=10)

        update_button = Button(frame, text="Update", command=self.edit_book)
        update_button.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [0, 0, 0]
        self.update_button = update_button  # Create(BUTTON)
        self.name = name
        self.score = score
        self.author = author

    def edit_book(self):
        book = self.master.treeview.focus()
        self.master.treeview.item(book, values=(
            int(self.score.get()),
            self.name.get().upper(),
            self.author.get().upper()
        ))
        mg.Books.modify_book(int(self.score.get()), self.name.get().upper(), self.author.get().upper())
        self.close()

    def close(self):
        self.destroy()
        self.update

    def validate(self, event, index):
        value = event.widget.get()
        valid = False
        if index == 0:
            try:
                valid = int(value) in list(range(1, 11))
                if valid:
                    event.widget.configure({"bg": "Green"})
                else:
                    event.widget.configure({"bg": "Red"})
            except ValueError:
                event.widget.configure({"bg": "Red"})

        if index == 1:
            valid = 2 <= len(value) <= 30
            if valid:
                event.widget.configure({"bg": "Green"})
            else:
                event.widget.configure({"bg": "Red"})

        if index == 2:
            valid = 2 <= len(value) <= 30
            if valid:
                event.widget.configure({"bg": "Green"})
            else:
                event.widget.configure({"bg": "Red"})


        self.validations[index] = valid
        self.update_button.config(state=NORMAL if self.validations == [1, 1, 1] else DISABLED)


class MainWindow(Tk, CenterWidgetMixing):
    def __init__(self):
        super().__init__()
        self.title('Books Manager')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('SCORE', 'NAME', 'AUTHOR')
        treeview.pack()

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("SCORE", anchor=CENTER)
        treeview.column("NAME", anchor=CENTER)
        treeview.column("AUTHOR", anchor=CENTER)

        treeview.heading("#0", anchor=CENTER)
        treeview.heading("SCORE", text="SCORE", anchor=CENTER)
        treeview.heading("NAME", text="NAME", anchor=CENTER)
        treeview.heading("AUTHOR", text="AUTHOR", anchor=CENTER)

        treeview.pack()

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=treeview.yview)
        treeview['yscrollcommand'] = scrollbar.set
        treeview.pack(side='left', fill='both', expand=True)

        for book in mg.Books.books_list:
            treeview.insert(
                parent='', index='end', iid=book.name,
                values=(book.score, book.name, book.author))

        treeview.pack()

        frame = Frame()
        frame.pack(pady=20)
        Button(frame, text="Add", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modify", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def delete(self):
        book = self.treeview.focus()
        if book:
            row = self.treeview.item(book, "values")
            confirm = askokcancel(
                title="Confirm to delete",
                message=f"Are you sure you want to delete the user {row[1]} {row[2]}?",
                icon=WARNING)
            if confirm:
                self.treeview.delete(book)
                mg.Books.delete_book(book)

    def create(self):
        Create_Book_Window(self)

    def edit(self):
        if self.treeview.focus():
            Modify_Book_Window(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
