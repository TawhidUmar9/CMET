from library_manager import LibraryManager
import datetime

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
        print("8. Get Book List")
        print("9. Get User List")
        print("10. Search Book")
        print("11. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = int(input("Enter the year of the book: "))
                publisher = input("Enter the publisher of the book: ")
                publication_date = datetime.datetime.strptime(input("Enter the publication date of the book: "), "%Y-%m-%d").date()
                number_of_copies = int(input("Enter the number of copies: "))
            except ValueError:
                print("Invalid input. Please try again")
                continue
            if library_manager.add_book( title, author, year, publisher, number_of_copies, publication_date):
                print("Book added successfully")
            else:
                print("Book could not be added")
        elif choice == "2":
            try:
                username = input("Enter the username: ")
                firstname = input("Enter the first name: ")
                surname = input("Enter the surname: ")
                house_number = input("Enter the house number: ")
                street_name = input("Enter the street name: ")
                post_code = input("Enter the post code: ")
                email = input("Enter the email: ")
                date_of_birth = datetime.datetime.strptime(input("Enter the date of birth: "), "%Y-%m-%d").date()
            except ValueError:
                print("Invalid input. Please try again")
                continue
            if library_manager.add_user(username, firstname, surname, house_number, street_name, post_code, email, date_of_birth):
                print("User added successfully")
            else:
                print("User could not be added")
        elif choice == "3":
            print("1. Modify Title")
            print("2. Modify Author")
            print("3. Modify Publisher")
            print("4. Modify Publication Date")
            print("5. Modify Number of Copies")
            try:
                sub_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please try again")
                continue
        
            if sub_choice == 1:
                title = input("Enter the title of the book: ")
                new_title = input("Enter the new title: ")
                if library_manager.modify_book_title(title, new_title):
                    print("Book title modified successfully")
                else:
                    print("Book title could not be modified")
            elif sub_choice == 2:
                title = input("Enter the title of the book: ")
                new_author = input("Enter the new author: ")
                if library_manager.modify_book_author(title, new_author):
                    print("Book author modified successfully")
                else:
                    print("Book author could not be modified")
            elif sub_choice == 3:
                title = input("Enter the title of the book: ")
                new_publisher = input("Enter the new publisher: ")
                if library_manager.modify_book_publisher(title, new_publisher):
                    print("Book publisher modified successfully")
                else:
                    print("Book publisher could not be modified")
            elif sub_choice == 4:
                try:
                    title = input("Enter the title of the book: ")
                    new_publication_date = datetime.datetime.strptime(input("Enter the new publication date: "), "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid input. Please try again")
                    continue
                if library_manager.modify_book_publication_date(title, new_publication_date):
                    print("Book publication date modified successfully")
                else:
                    print("Book publication date could not be modified")
            elif sub_choice == 5:
                title = input("Enter the title of the book: ")
                new_number_of_copies = int(input("Enter the new number of copies: "))
                if library_manager.modify_book_number_of_copies(title, new_number_of_copies):
                    print("Book number of copies modified successfully")
                else:
                    print("Book number of copies could not be modified")
        elif choice == "4":
            print("1. Modify Firstname")
            print("2. Modify Surname")
            print("3. Modify House Number")
            print("4. Modify Street Name")
            print("5. Modify Post Code")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                username = input("Enter the username: ")
                new_firstname = input("Enter the new first name: ")
                if library_manager.modify_user_firstname(username, new_firstname):
                    print("User first name modified successfully")
                else:
                    print("User first name could not be modified")
            elif sub_choice == 2:
                username = input("Enter the username: ")
                new_surname = input("Enter the new surname: ")
                if library_manager.modify_user_surname(username, new_surname):
                    print("User surname modified successfully")
                else:
                    print("User surname could not be modified")
            elif sub_choice == 3:
                username = input("Enter the username: ")
                new_house_number = input("Enter the new house number: ")
                if library_manager.modify_user_house_number(username, new_house_number):
                    print("User house number modified successfully")
                else:
                    print("User house number could not be modified")
            elif sub_choice == 4:
                username = input("Enter the username: ")
                new_street_name = input("Enter the new street name: ")
                if library_manager.modify_user_street_name(username, new_street_name):
                    print("User street name modified successfully")
                else:
                    print("User street name could not be modified")
            elif sub_choice == 5:
                username = input("Enter the username: ")
                new_post_code = input("Enter the new post code: ")
                if library_manager.modify_user_post_code(username, new_post_code):
                    print("User post code modified successfully")
                else:
                    print("User post code could not be modified")
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
            overdued_book = library_manager.get_overdued_books()
            if overdued_book.__len__() == 0:
                print("No overdued books found")
            for book in overdued_book:
                print("Username: %s, Firstname: %s, Number of borrowed books: %d" % (book[0], book[1], book[2]))
        elif choice == "8":
            book_list = library_manager.get_book_list()
            ## book_list is a dictionary
            if book_list.__len__() == 0:
                print("No books found")
            for book in book_list.values():
                print("Title: " + book.get_title() + ", Author: " + book.get_author() + ", Year: " + str(book.get_year()) +\
                       ",Publisher: " + book.get_publisher() + ", Publication Date: " + str(book.get_publication_date()) + \
                        ", Number of Copies: " + str(book.get_number_of_available_copies()))
        elif choice == "9":
            user_list = library_manager.get_user_list()
            ## user_list is a dictionary
            if user_list.__len__() == 0:
                print("No users found")
            for user in user_list.values():
                print("Username: " + user.get_username() + ", Firstname: " + user.get_firstname() + ", Surname: " + user.get_surname() + \
                      ", House Number: " + user.get_house_number() + ", Street Name: " + user.get_street_name() + ", Post Code: " +\
                          user.get_post_code() + ", Email: " + user. get_email_address() + ", Date of Birth: " +\
                              str(user.get_date_of_birth()))
        elif choice == "10":
            try:
                print("1. Search by Title")
                print("2. Search by Author")
                print("3. Search by Publisher")
                print("4. Search by Publication Date")
                sub_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please try again")
                continue
            if sub_choice == 1:
                book = library_manager.search_book_by_title(input("Enter the title of the book: "))
                if book is None:
                    print("Book not found")
                else:
                    print("Title: " + book.get_title() + ", Author: " + book.get_author() + ", Year: " + str(book.get_year()) +\
                       ",Publisher: " + book.get_publisher() + ", Publication Date: " + str(book.get_publication_date()) + \
                        ", Number of Copies: " + str(book.get_number_of_available_copies()))
            elif sub_choice == 2:
                book = library_manager.search_book_by_author(input("Enter the author of the book: "))
                if book is None:
                    print("Book not found")
                else:
                    print("Title: " + book.get_title() + ", Author: " + book.get_author() + ", Year: " + str(book.get_year()) +\
                       ",Publisher: " + book.get_publisher() + ", Publication Date: " + str(book.get_publication_date()) + \
                        ", Number of Copies: " + str(book.get_number_of_available_copies()))
            elif sub_choice == 3:
                book = library_manager.search_book_by_publisher(input("Enter the publisher of the book: "))
                if book is None:
                    print("Book not found")
                else:
                    print("Title: " + book.get_title() + ", Author: " + book.get_author() + ", Year: " + str(book.get_year()) +\
                       ",Publisher: " + book.get_publisher() + ", Publication Date: " + str(book.get_publication_date()) + \
                        ", Number of Copies: " + str(book.get_number_of_available_copies()))
            elif sub_choice == 4:
                book = library_manager.search_book_by_publication_date(datetime.datetime.strptime(input("Enter the publication date of the book: "), "%Y-%m-%d").date())
                if book is None:
                    print("Book not found")
                else:
                    print("Title: " + book.get_title() + ", Author: " + book.get_author() + ", Year: " + str(book.get_year()) +\
                       ",Publisher: " + book.get_publisher() + ", Publication Date: " + str(book.get_publication_date()) + \
                        ", Number of Copies: " + str(book.get_number_of_available_copies()))
        elif choice == "11":
            print("Exiting the Library Management System")
            break
        else:
            print("Invalid choice. Please try again")

init = main()