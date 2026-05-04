from add_book import add_book
from issue_book import issue_book
from return_book import return_book
from show_book import show_book

def menu():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Show Book")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_book()
        elif choice == "2":
            add_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

menu()