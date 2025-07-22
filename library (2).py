import os
import pickle
from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' by {author} added successfully.")

    def issue_book(self, title, member_name):
        for book in self.books:
            if book.title == title and book.issued_to is None:
                book.issued_to = member_name
                self.save_books()
                print(f"Book '{title}' issued to {member_name}.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title, member_name):
        for book in self.books:
            if book.title == title and book.issued_to == member_name:
                book.issued_to = None
                self.save_books()
                print(f"Book '{title}' returned by {member_name}.")
                return
        print(f"Book '{title}' was not issued to {member_name}.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(book)

    def save_books(self):
        with open("books.pkl", "wb") as f:
            pickle.dump(self.books, f)

    def load_books(self):
        if os.path.exists("books.pkl"):
            with open("books.pkl", "rb") as f:
                self.books = pickle.load(f)
        else:
            self.books = []







