
# Library Management System with Database Integration

This is a command-line-based Library Management System that integrates with a MySQL database to manage books and users. The system allows users to browse, borrow, return, and explore a collection of books, demonstrating proficiency in database integration, SQL, and Python.

## Features

- **Add Books**: Add new books to the library.
- **Borrow Books**: Borrow books from the library.
- **Return Books**: Return borrowed books to the library.
- **Search Books**: Search for books by title.
- **Display All Books**: Display all books in the library.
- **Add Users**: Add new users to the library system.
- **View User Details**: View details of a specific user.
- **Display All Users**: Display all users in the library system.

## Requirements

- Python 3.x
- MySQL Server
- mysql-connector-python

## Setup

### Install Dependencies

Install the required Python package using pip:
```bash
pip install mysql-connector-python
```

### MySQL Database Setup

1. **Start MySQL Server**: Ensure your MySQL server is running.
2. **Create Database and Tables**:
   ```sql
   CREATE DATABASE library_management;

   USE library_management;

   CREATE TABLE books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       isbn VARCHAR(13) NOT NULL,
       publication_date DATE,
       availability BOOLEAN DEFAULT 1
   );

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(250) NOT NULL UNIQUE
   );

   CREATE TABLE borrowed_books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT,
       book_id INT,
       borrow_date DATE NOT NULL,
       return_date DATE,
       FOREIGN KEY (user_id) REFERENCES users(id),
       FOREIGN KEY (book_id) REFERENCES books(id)
   );
   ```

### Configuration

Update the database connection settings in `database_operations.py`:
```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='library_management'
)
```

Replace `your_username` and `your_password` with your MySQL username and password.

## Running the Application

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Run the Script**:
   ```bash
   python database_operations.py
   ```

## Usage

Follow the on-screen instructions to navigate through the menus and perform various operations.

### Main Menu

1. Book Operations
2. User Operations
3. Quit

### Book Operations

1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books

### User Operations

1. Add a new user
2. View user details
3. Display all users

## Example

Example interaction:
1. Add a new book:
   - Enter book title: The Great Gatsby
   - Enter ISBN: 1234567890123
   - Enter publication date (YYYY-MM-DD): 1925-04-10
   - Output: Book added successfully

2. Display all books:
   - Output: 
     ```
     (1, 'The Great Gatsby', '1234567890123', '1925-04-10', 1)
     ```

## Error Handling

- Uses try, except, else, and finally blocks to manage errors gracefully.
- Handles exceptions related to database operations, input validation, and other potential issues.
- Provides informative error messages to guide users.

## Code Structure

- `database_operations.py`: Contains all the functions for database operations.
- `README.md`: Documentation file.

## Clean Code Principles

- Meaningful variable and function names that convey their purpose.
- Clear comments and docstrings explaining the functionality of functions and classes.
- Follows PEP 8 style guidelines for code formatting and structure.
- Proper indentation and spacing for readability.

## Modular Design

- Separate modules for database operations, user interactions, error handling, and core functionalities to promote modularity and maintainability.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

