from datetime import datetime
import mysql.connector

class library_management():

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="sqluser",     
            password="password",
            database="library_db"
        )
        self.connection.cursor().execute("CREATE DATABASE LIBRARY_DB IF NOT EXISTS")
        self.connection.curosr().execute("use LIBRARY_DB")
        self.connection.cursor().execute('''CREATE TABLE IF NOT EXISTS Books (
                        book_id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        author VARCHAR(255) NOT NULL,
                        status ENUM('available', 'issued') NOT NULL DEFAULT 'available')''')

        self.connection.cursor().execute('''CREATE TABLE IF NOT EXISTS Borrowers (
                            borrower_id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            contact VARCHAR(255) UNIQUE )''')

        self.connection.cursor().execute('''CREATE TABLE IF NOT EXISTS Transactions (
                            transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                            book_id INT,
                            borrower_id INT,
                            issue_date DATETIME,
                            return_date DATETIME,
                            FOREIGN KEY (book_id) REFERENCES Books(book_id),
                            FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id))''')
        
    def search(self,name,contact):
        cursor = self.connection.cursor()
        query = '''
        SELECT books.book_id ,transactions.issue_date, borrowers.name,books.title
        FROM borrowers
        left JOIN transactions ON borrowers.borrower_id = transactions.borrower_id 
        JOIN books ON transactions.book_id = books.book_id where borrowers.name = %s and borrowers.contact = %s
        '''
        
        cursor.execute(query,(name,contact,))  
        results = cursor.fetchall()  
        if results:
            for book_id, issue_date, name ,title in results: 
                return book_id, issue_date, name,f"{name} borrowed the Book {title} On {issue_date}"
        else:
            print("Name and email not found in the database.")
            return None, None,None,None
        
    def add_book(self,title, author):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO Books (title, author) VALUES (%s, %s)', (title, author))
        self.connection.commit()
    
    def add_borrower(self):
        try:
            cursor = self.connection.cursor()
            print("==========================REGISTRATION FORM===============================")
            name = input("Enter your name: ")
            contact = input("Enter your email: ")
            cursor.execute('INSERT INTO Borrowers (name, contact) VALUES (%s, %s)', (name, contact))
            self.connection.commit()
            print(f"Thank you, {name}, you are successfully registered.")
            
        except mysql.connector.errors.IntegrityError:
            print("You are not registered again.")
    
    def return_book(self):
        name = input("Enter your name: ")
        contact = input("Enter your email: ")
        cursor = self.connection.cursor()
        book_id, issue_date, name,check = self.search(name,contact)
        
        if check:
            print(check)
            return_date = datetime.now()
            difference = (datetime.now() - issue_date).days

            if difference > 3:
                print("Due to your late submission, a penalty has been applied.")
            cursor.execute('UPDATE Books SET status = "available" WHERE book_id = %s', (book_id,))
            cursor.execute('UPDATE Transactions SET return_date = %s WHERE book_id = %s AND return_date IS NULL', 
                        (return_date, book_id))
            self.connection.commit()

            if difference <= 3:
                print("---------------------------------------------------")
                print(f"Thank you, {name}, for returning the book on time.")
    
    def issue_book(self, borrower_id,user_email):
        cursor = self.connection.cursor()

        try:
            
            cursor.execute("select contact from borrowers where borrower_id = %s", (borrower_id,))
            borrower_email = cursor.fetchone()[0]
            print(borrower_email)

            if user_email == borrower_email:
                list_of_book = input("would you like see list of available book (y/n): ").lower()

                if list_of_book == 'y':
                    self.view_available_books()
                book_id = input("Enter your choice of book ID: ")
                cursor.execute('SELECT status FROM Books WHERE book_id = %s', (book_id,))
                status = cursor.fetchone()[0]
                
                if status == 'available':
                    issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute('UPDATE Books SET status = "issued" WHERE book_id = %s', (book_id,))
                    cursor.execute('INSERT INTO Transactions (book_id, borrower_id, issue_date) VALUES (%s, %s, %s)', 
                                (book_id, borrower_id, issue_date))
                    self.connection.commit()
                    cursor.execute("select name from borrowers where borrower_id = %s", (borrower_id,))
                    name = cursor.fetchone()[0] 
                    print("||---------------------------------------------------------------------||")
                    print(f"||           {name}, you have successfully borrow the BOOK.          ")
                    print("||_____________________________________________________________________||")

            else:
                print("You are not registerd or Inccorect input !!")
        except TypeError as e:
            print(e)


    def view_available_books(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Books WHERE status = "available"')
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    print("==========================LIBRARY MANAGEMENT SYSTEM======================")
