import file_operations

def find_book():
    books = file_operations.load_books()
    keyword = input("Enter title or author to search: ").lower()
    
    found_books = [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]
    
    if not found_books:
        print("No matching books found.")
        return
    
    print("\nSearch Results:")
    for book in found_books:
        print(f"- {book['title']} by {book['author']} (Genre: {book['genre']}, Price: ${book['price']}, Stock: {book['quantity']})")
