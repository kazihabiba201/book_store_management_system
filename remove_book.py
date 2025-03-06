import file_operations

def delete_book():
    books = file_operations.load_books()
    
    isbn = input("Enter ISBN/Book ID of the book to remove: ")
    
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            file_operations.save_books(books)
            print("Book removed successfully!")
            return
    
    print("Book not found.")
