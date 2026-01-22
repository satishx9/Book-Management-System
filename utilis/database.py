books = []


def get_all_books():
    return books


def insert_book(name, author, description, price):
    books.append({
        "name": name,
        "author": author,
        "description": description,
        "price": int(price),
        "read": False
    })


def mark_book_as_read(name):
    for book in books:
        if book["name"].lower() == name.lower():
            book["read"] = True
            return True
    return False


def delete_book(name):
    global books
    original_length = len(books)
    books = [book for book in books if book["name"].lower() != name.lower()]
    return len(books) < original_length


def search_book(name):
    for book in books:
        if book["name"].lower() == name.lower():
            return book
    return None


def update_price(name, price):
    for book in books:
        if book["name"].lower() == name.lower():
            book["price"] = int(price)
            return True
    return False


def sort_books_by_price():
    books.sort(key=lambda x: x["price"])
