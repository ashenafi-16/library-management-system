Library Management System

Overview

The Library Management System is a Python-based project designed to manage a library's key operations, including adding and listing books, borrower registration, and handling borrowing and penalty systems. The system streamlines the process of borrowing books and keeps track of penalties for late returns.

Features

1. Add Book 
   - Admins can add new books to the system, which will then be available for borrowing.

2. List Available Books
   - The system allows users to view a list of all books that are currently available in the library.

3. Borrower Registration
   - New borrowers can be registered with the system. This ensures that only registered users can borrow books from the library.

4. Borrow Books
   - Registered borrowers can borrow books from the library. The system tracks the borrowing date for each book.

5. Penalty System for Late Returns 
   - If a borrower returns a book more than 3 days after the borrowing date, the system will automatically apply a penalty. This ensures timely returns and availability of books for other users.

How It Works

1. Adding Books
   - Library staff can add new books to the collection, which will be available for borrowers. Each book is stored with its details (e.g., title, author).

2. Borrowing Books 
   - Once registered, borrowers can select books to borrow. The system records the borrowing date and calculates whether the book is returned on time.

3. Penalty for Late Returns 
   - If a book is returned after 3 days, the system automatically calculates a penalty, encouraging borrowers to return books on time.

Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Install the necessary dependencies:
   ```bash
   pip install mysql-connector-python
   ```

4. Run the application:
   ```bash
   python server.py
   ```

Usage

- Add Books: Use the system's interface to add new books to the library.
- Register Borrowers: Register new borrowers by entering their details.
- Borrow Books: Borrowers can borrow books, and the system tracks their borrowing date.
- Late Penalty: If a book is not returned within 3 days, the system will apply a penalty.

Future Enhancements

- Enhance the user interface for better interaction.
- Implement notifications for borrowers to remind them of return dates.
- Add a feature to reserve books.

