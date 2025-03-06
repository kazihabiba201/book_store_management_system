import add_book
import view_books
import search_book
import remove_book
import file_operations

def main_menu():
    while True:
        print("Book Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book.add_new_book()
        elif choice == "2":
            view_books.display_books()
        elif choice == "3":
            search_book.find_book()
        elif choice == "4":
            remove_book.delete_book()
        elif choice == "5":
            print("Exiting...System")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    file_operations.load_books() 
    main_menu()
