class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued_to = None

    def __str__(self):
        status = f"Issued to: {self.issued_to}" if self.issued_to else "Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"
