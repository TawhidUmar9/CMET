from books import Book
from book_list import BookList
from user import User
from users_list import UsersList
from loan import Loan
import random

class LibraryManager:
    
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UsersList()
        self.loan = Loan()
        self.book_id = {}
    
    def add_book(self, title, author, year, publisher, number_of_available_copies, publication_date):
        book_id = 0
        while True:
            book_id = random.randint(1000, 9999)
            if book_id not in self.book_id:
                break
        book = Book(book_id,  title, author, year, publisher, number_of_available_copies, publication_date)
        return self.book_list.add_book(book)

    def add_user(self,username, firstname, surname, house_number, street_name, post_code, email_address, date_of_birth):
        user = User(username, firstname, surname, house_number, street_name, post_code, email_address, date_of_birth)
        return self.user_list.add_user(user)
    
    def modify_book_title(self, title, new_title):
        return self.book_list.modify_book_title(title, new_title)
    def modify_book_author(self, title, new_author):
        return self.book_list.modify_book_author(title, new_author)
    def modify_book_publisher(self, title, new_publisher):
        return self.book_list.modify_book_publisher(title, new_publisher)
    def modify_book_publication_date(self, title, new_publication_date):
        return self.book_list.modify_book_publication_date(title, new_publication_date)
    def modify_book_number_of_copies(self, title, new_number_of_copies):
        return self.book_list.modify_book_number_of_copies(title, new_number_of_copies)
    
    def modify_user_firstname(self, username, new_firstname):
        return self.user_list.modify_user_firstname(username, new_firstname)
    def modify_user_surname(self, username, new_surname):
        return self.user_list.modify_user_surname(username, new_surname)
    def modify_user_house_number(self, username, new_house_number):
        return self.user_list.modify_user_house_number(username, new_house_number)
    def modify_user_street_name(self, username, new_street_name):
        return self.user_list.modify_user_street_name(username, new_street_name)
    def modify_user_postcode(self, username, new_postcode):
        return self.user_list.modify_user_postcode(username, new_postcode)
    
    def search_book_by_title(self, title):
        return self.book_list.search_book_by_title(title)
    def search_book_by_author(self, author):
        return self.book_list.search_book_by_author(author)
    def search_book_by_publisher(self, publisher):
        return self.book_list.search_book_by_publisher(publisher)
    def search_book_by_publication_date(self, publication_date):
        return self.book_list.search_book_by_publication_date(publication_date)
    

    def borrow_book(self, username, title):
        user = self.user_list.search_user_by_username(username)
        book = self.book_list.search_book_by_title(title)
        if user is None or book is None:
            return False
        return self.loan.borrow_book(username, book)
    
    def return_book(self, username, title):
        user = self.user_list.search_user_by_username(username)
        book = self.book_list.search_book_by_title(title)
        if user is None or book is None:
            return False
        return self.loan.return_book(username, book)
    
    def get_overdued_books(self):
        return self.loan.get_overdued_books(self.user_list)
    
    def get_borrowed_books_count(self, username):
        return self.loan.get_borrowed_books_count(username)
    
    def get_book_list(self):
        return self.book_list.books
    
    def get_user_list(self):
        return self.user_list.users