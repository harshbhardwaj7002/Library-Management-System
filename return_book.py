from utils import library, issued_books
from datetime import datetime

def return_book():
    user = input("Enter user name: ")

    if user in issued_books:
        book_id = issued_books[user]["book_id"]
        issue_date = issued_books[user]["date"]

        days = (datetime.now() - issue_date).days

        library[book_id]["available"] = True
        del issued_books[user]

        print("Book returned successfully!")
        print(f"Days used: {days}")

        if days > 7:
            fine = (days - 7) * 5
            print(f"Late return! Fine = ₹{fine}")
        else:
            print("No fine!")
    else:
        print("No record found!")