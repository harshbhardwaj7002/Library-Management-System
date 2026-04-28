# issue_book.py

from utils import library, issued_books
from datetime import datetime

def issue_book():
    book_id = int(input("Enter book ID: "))
    user = input("Enter user name: ")

    if book_id in library and library[book_id]["available"]:
        library[book_id]["available"] = False

        issued_books[user] = {
            "book_id": book_id,
            "date": datetime.now()
        }

        print("Book issued successfully!")
    else:
        print("Book not available!")