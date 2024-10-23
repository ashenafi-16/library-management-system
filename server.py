from project import library_management
Library = library_management()
while True:
    choice = int(input("""
    1. ADD BOOKS
    2. VIEW AVAILABLE BOOKS
    3. RETURN BOOK
    4. iSSUES BOOK
    5. BORROWER INFORMATION
    6. EXIT 
    """))

    if choice == 1:
        title = input("enter the title of the book: ")
        author = input("enter the book author: ")
        Library.add_book(title,author)

    elif choice == 2:
        Library.view_available_books()

    elif choice == 3:
        
        Library.return_book()

    elif choice == 4:
        borrower_id = input("Enter your ID: ")
        user_email = input("Enter your email: ")
        Library.issue_book(borrower_id,user_email)

    elif choice == 5:
        
        Library.add_borrower()

    elif choice == 6:
        print("=====================================================================\n GOOD BYE!")
        Library.close_connection()
        exit()

    else:
        print("Incorrect input please try again!!")
