class Loan:
    def __init__(self):
        self.borrowed_books = {} ## Storing the borrowed books in a dictionary. Key is the username and value is a list of books
    
    def borrow_book(self, username, book):
        ## If the user has not borrowed any books yet, create an empty list
        if username not in self.borrowed_books:
            self.borrowed_books[username] = []
        ## Append the book to the list of borrowed books
        if(book.title not in self.borrowed_books[username] and book.get_number_of_available_copies() > 0):
            self.borrowed_books[username].append(book)
            book.set_number_of_available_copies(book.get_number_of_available_copies() - 1)
            return True
        return False
    
    def return_book(self, username, book):
        ## If the user has not borrowed any books yet, return False
        if username not in self.borrowed_books:
            return False
        ## If the book is not in the list of borrowed books, return False
        if book not in self.borrowed_books[username]:
            return False
        ## Remove the book from the list of borrowed books
        self.borrowed_books[username].remove(book)
        book.set_number_of_available_copies(book.get_number_of_available_copies() + 1)
        return True
    
    def get_borrowed_books_count(self, username):
        ## If the user has not borrowed any books yet, return count = 0
        if username not in self.borrowed_books:
            return 0
        ## Return the count of borrowed books
        return len(self.borrowed_books[username])
    
    def get_overdued_books(self, user_list):
        ## Just pass the username, first name and the borrowed book count
        overdued_books = []
        for username in self.borrowed_books:
            user = user_list.search_user_by_username(username)
            if user is None:
                continue
            overdued_books.append((user.get_username(), user.get_first_name(), len(self.borrowed_books[username])))
                