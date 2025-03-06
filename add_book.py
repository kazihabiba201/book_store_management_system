import json
import file_operations

def add_new_book():
    books = file_operations.load_books()
    
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN/Book ID (must be unique): ")
    genre = input("Enter book genre: ")
    
    try:
        price = float(input("Enter book price: "))
        quantity = int(input("Enter quantity in stock: "))
        
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        for book in books:
            if book["isbn"] == isbn:
                print("Book with this ISBN already exists.")
                return

        new_book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "price": price,
            "quantity": quantity
        }

        books.append(new_book)
        file_operations.save_books(books)
        print("Book added successfully!")
    
    except ValueError as e:
        print(f"Error: {e}")
