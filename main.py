
from database_operations import (
    create_connection, add_book, borrow_book, return_book,
    search_books_by_title, display_all_books,
    add_user, view_user_details, display_all_users
)

def main_menu():
    print("Welcome to the Library Management System with Database Integration!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Quit")
    return input("Select an option: ")

def book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    return input("Select an option: ")

def user_operations_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    return input("Select an option: ")

def main():
    connection = create_connection()

    while True:
        choice = main_menu()
        if choice == '1':
            book_choice = book_operations_menu()
            if book_choice == '1':
                title = input("Enter book title: ")
                isbn = input("Enter ISBN: ")
                publication_date = input("Enter publication date (YYYY-MM-DD): ")
                add_book(connection, title, isbn, publication_date)
            elif book_choice == '2':
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
                borrow_book(connection, user_id, book_id, borrow_date)
            elif book_choice == '3':
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                return_date = input("Enter return date (YYYY-MM-DD): ")
                return_book(connection, user_id, book_id, return_date)
            elif book_choice == '4':
                title = input("Enter book title to search: ")
                search_books_by_title(connection, title)
            elif book_choice == '5':
                display_all_books(connection)
        elif choice == '2':
            user_choice = user_operations_menu()
            if user_choice == '1':
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                add_user(connection, name, email)
            elif user_choice == '2':
                user_id = int(input("Enter user ID: "))
                view_user_details(connection, user_id)
            elif user_choice == '3':
                display_all_users(connection)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
