from utils import library

def show_book():
    if not library:
        print("No books in library")
        return

    print("\nLibrary Books:")
    for book_id, info in library.items():
        status = "Available" if info["available"] else "Issued"
        print(f"ID: {book_id} | Name: {info['name']} | {status}")