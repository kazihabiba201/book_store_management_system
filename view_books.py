import file_operations

def display_books():
    books = file_operations.load_books()
    
    if not books:
        print("No books available.")
        return
    
    print("\n Available Books:")
    for book in books:
        print(f"- {book['title']} by {book['author']} (Genre: {book['genre']}, Price: ${book['price']}, Stock: {book['quantity']})")
