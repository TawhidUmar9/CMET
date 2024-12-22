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
    