import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mysql123!',
            database='library_management'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Establish connection
connection = create_connection()

def add_book(connection, title, isbn, publication_date):
    cursor = connection.cursor()
    query = "INSERT INTO books (title, isbn, publication_date) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (title, isbn, publication_date))
        connection.commit()
        print("Book added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def borrow_book(connection, user_id, book_id, borrow_date):
    cursor = connection.cursor()
    update_book_query = "UPDATE books SET availability = 0 WHERE id = %s"
    insert_borrow_query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
    try:
        cursor.execute(update_book_query, (book_id,))
        cursor.execute(insert_borrow_query, (user_id, book_id, borrow_date))
        connection.commit()
        print("Book borrowed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def return_book(connection, user_id, book_id, return_date):
    cursor = connection.cursor()
    update_book_query = "UPDATE books SET availability = 1 WHERE id = %s"
    update_borrow_query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s"
    try:
        cursor.execute(update_book_query, (book_id,))
        cursor.execute(update_borrow_query, (return_date, user_id, book_id))
        connection.commit()
        print("Book returned successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def search_books_by_title(connection, title):
    cursor = connection.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s"
    try:
        cursor.execute(query, ('%' + title + '%',))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def display_all_books(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM books"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def add_user(connection, name, email):
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    try:
        cursor.execute(query, (name, email))
        connection.commit()
        print("User added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def view_user_details(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    try:
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        print(result)
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def display_all_users(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()




add_book(connection, "The Great Gatsby", "1234567890123", "1925-04-10")
if connection and connection.is_connected():
    connection.close()
    print("The connection is closed")
