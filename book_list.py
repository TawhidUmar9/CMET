class BookList:
    ## books is a dictionary with the book title as the key
    def __init__(self):
        ## Storing the books in a dictionary
        self.books = {}
    
    def add_book(self, book):
        ## Using the book title as the key
        ## If the book title already exists, return False
        if book.get_title() in self.books:
            return False
        self.books[book.get_title()] = book
        return True  # Return True when book is successfully added
    
    def remove_book(self, title):
        if title == "":
            return False
        ## Remove the book by its title
        if title in self.books:
            del self.books[title]  # Delete the book using its title
            return True
        return False
    
    def search_book_by_title(self, title):
        if title == "":
            return None
        ## Seach for a book by its title and return it if found
        return self.books.get(title, None)
    
    def search_book_by_author(self, author):
        if author == "":
            return None
        ## Search for a book by its author and return it if found
        for book in self.books.values():
            if book.get_author() == author:
                return book
        return None
    
    def search_book_by_publisher(self, publisher):
        if publisher == "":
            return None
        ## Search for a book by its publisher and return it if found
        for book in self.books.values():
            if book.get_publisher() == publisher:
                return book
        return None
    
    def search_book_by_publication_date(self, publication_date):
        if publication_date == "":
            return None
        ## Search for a book by its publication date and return it if found
        for book in self.books.values():
            if book.get_publication_date() == publication_date:
                return book
        return None
    
    def get_book_count(self):
        # Return the number of books in the dictionary
        return len(self.books)
    
    def modify_book_title(self, title, new_title):
        book = self.search_book_by_title(title)
        if book is None:
            return False
        self.books[new_title] = self.books.pop(title)
        book.set_title(new_title)
        return True
    def modify_book_author(self, title, new_author):
        book = self.search_book_by_title(title)
        if book is None:
            return False
        book.set_author(new_author)
        return True
    def modify_book_publisher(self, title, new_publisher):
        book = self.search_book_by_title(title)
        if book is None:
            return False
        book.set_publisher(new_publisher)
        return True
    def modify_book_publication_date(self, title, new_publication_date):
        book = self.search_book_by_title(title)
        if book is None:
            return False
        book.set_publication_date(new_publication_date)
        return True
    def modify_book_number_of_copies(self, title, new_number_of_copies):
        book = self.search_book_by_title(title)
        if book is None:
            return False
        if new_number_of_copies < 0:
            return False
        book.set_number_of_available_copies(new_number_of_copies)
        return True
    