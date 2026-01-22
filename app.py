from utilis import database

MENU = """
BOOK MANAGEMENT SYSTEM

Choose an option:
[a] Add a new book
[l] List all books
[r] Mark a book as read
[d] Delete a book
[s] Search for a book
[u] Update book price
[sort] Sort books by price
[q] Quit

Your choice: """


def menu():
    choice = input(MENU).strip().lower()

    while choice != "q":
        if choice == "a":
            add_book()
        elif choice == "l":
            list_books()
        elif choice == "r":
            mark_read()
        elif choice == "d":
            delete_book()
        elif choice == "s":
            search_book()
        elif choice == "u":
            update_price()
        elif choice == "sort":
            sort_books()
        else:
            print("Invalid choice. Please try again.")

        choice = input(MENU).strip().lower()

    print("\nThank you for using Book Management System!")


def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    description = input("Enter description: ")

    try:
        price = int(input("Enter price: "))
    except ValueError:
        print("Price must be a number.")
        return

    database.insert_book(name, author, description, price)
    print("Book added successfully.")


def list_books():
    books = database.get_all_books()

    if not books:
        print("No books available. Please add some books first.")
        return

    print("\nAvailable Books:")
    print("-" * 60)
    for book in books:
        read_status = "YES" if book["read"] else "NO"
        print(
            f"{book['name']} by {book['author']} "
            f"| Read: {read_status} "
            f"| Description: {book['description']} "
            f"| Price: ${book['price']}"
        )
        print("-" * 60)


def mark_read():
    name = input("Enter the book name to mark as read: ")

    if database.mark_book_as_read(name):
        print("Book marked as read.")
    else:
        print("Book not found.")


def delete_book():
    name = input("Enter the book name to delete: ")

    if database.delete_book(name):
        print(f"{name} deleted successfully.")
    else:
        print("Book not found.")


def search_book():
    name = input("Enter the book name to search: ")
    book = database.search_book(name)

    if book:
        read_status = "YES" if book["read"] else "NO"
        print("\nBook Found:")
        print(f"Name        : {book['name']}")
        print(f"Author      : {book['author']}")
        print(f"Price       : ${book['price']}")
        print(f"Read        : {read_status}")
        print(f"Description : {book['description']}")
    else:
        print("Book not found.")


def update_price():
    name = input("Enter the book name: ")

    try:
        price = int(input("Enter the new price: "))
    except ValueError:
        print("Price must be a number.")
        return

    if database.update_price(name, price):
        print("Price updated successfully.")
    else:
        print("Book not found.")


def sort_books():
    database.sort_books_by_price()
    print("Books sorted by price (low to high).")
    list_books()


menu()
