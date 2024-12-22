from library_manager import LibraryManager

def main():
    library_manager = LibraryManager()
    print("Welcome to the Library Management System")
    while True:
        print("1. Add Book")
        print("2. Add User")
        print("3. Modify Book")
        print("4. Modify User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Get Overdued Books")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publisher = input("Enter the publisher of the book: ")
            publication_date = input("Enter the publication date of the book: ")
            number_of_copies = int(input("Enter the number of copies: "))
            if library_manager.add_book(title, author, publisher, publication_date, number_of_copies):
                print("Book added successfully")
            else:
                print("Book could not be added")
        elif choice == "2":
            username = input("Enter the username: ")
            firstname = input("Enter the first name: ")
            lastname = input("Enter the last name: ")
            email = input("Enter the email: ")
            if library_manager.add_user(username, firstname, lastname, email):
                print("User added successfully")
            else:
                print("User could not be added")
        elif choice == "3":
            title = input("Enter the title of the book: ")
            new_title = input("Enter the new title of the book: ")
            if library_manager.modify_book_title(title, new_title):
                print("Book title modified successfully")
            else:
                print("Book title could not be modified")
        elif choice == "4":
            username = input("Enter the username: ")
            new_firstname = input("Enter the new first name: ")
            if library_manager.modify_user_firstname(username, new_firstname):
                print("User first name modified successfully")
            else:
                print("User first name could not be modified")
        elif choice == "5":
            username = input("Enter the username: ")
            title = input("Enter the title of the book: ")
            if library_manager.borrow_book(username, title):
                print("Book borrowed successfully")
            else:
                print("Book could not be borrowed")
        elif choice == "6":
            username = input("Enter the username: ")
            title = input("Enter the title of the book: ")
            if library_manager.return_book(username, title):
                print("Book returned successfully")
            else:
                print("Book could not be returned")
        elif choice == "7":
            library_manager.get_overdued_books()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again")
