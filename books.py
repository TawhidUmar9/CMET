import datetime

class Book:
    ## bookID: int
    ## title: string
    ## author: string
    ## year: int
    ## publisher: string
    ## number_of_available_copies: int
    ## publication_date: date

    def __init__(self, book_id, title, author, year, publisher, number_of_available_copies, publication_date):
        self.bookID = book_id
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.number_of_available_copies = number_of_available_copies
        self.publication_date = publication_date

    # General setter method for validation
    def _validate_string(self, value, max_length=100):
        """Helper method to validate string inputs."""
        if not value:
            raise ValueError("Value cannot be empty.")
        if len(value) > max_length:
            raise ValueError(f"Value cannot be longer than {max_length} characters.")
        return value

    def set_title(self, title):
        self.title = self._validate_string(title)
    
    def set_author(self, author):
        self.author = self._validate_string(author)
    
    def set_publisher(self, publisher):
        self.publisher = self._validate_string(publisher)

    def set_year(self, year):
        if year < 0:
            raise ValueError("Year cannot be negative.")
        if year > datetime.datetime.now().year:
            raise ValueError("Year cannot be in the future.")
        self.year = year

    def set_number_of_available_copies(self, number_of_available_copies):
        if number_of_available_copies < 0:
            raise ValueError("Number of available copies cannot be negative.")
        self.number_of_available_copies = number_of_available_copies

    def set_publication_date(self, publication_date):
        if publication_date > datetime.date.today():
            raise ValueError("Publication date cannot be in the future.")
        self.publication_date = publication_date

    # Getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_number_of_available_copies(self):
        return self.number_of_available_copies

    def get_publication_date(self):
        return self.publication_date
