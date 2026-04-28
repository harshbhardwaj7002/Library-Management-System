from utils import library

def add_book():
    name = input("Enter book name: ")

    book_id = len(library) + 1

    library[book_id] = {
        "name": name,
        "available": True
    }

    print(f"Book added! ID = {book_id}")