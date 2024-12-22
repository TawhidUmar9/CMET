from books import Book
from book_list import BookList
from user import User
from users_list import UsersList
from loan import Loan
import random

class Library:
    
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UsersList()
        self.loan = Loan()
        self.book_id = {}
    
    def add_book(self, title, author, publisher, publication_date, number_of_copies):
        book_id = 0
        while True:
            book_id = random.randint(1000, 9999)
            if book_id not in self.book_id:
                break
        book = Book(book_id, title, author, publisher, publication_date, number_of_copies)
        return self.book_list.add_book(book)

    def add_user(self, username, firstname, lastname, email):
        user = User(username, firstname, lastname, email)
        return self.user_list.add_user(user)
    
    def modify_book_title(self, title, new_title):
        book = self.book_list.search_book_by_title(title)
        if book is None:
            return False
        book.set_title(new_title)
        return True
    def modify_book_author(self, title, new_author):
        book = self.book_list.search_book_by_title(title)
        if book is None:
            return False
        book.set_author(new_author)
        return True
    def modify_book_publisher(self, title, new_publisher):
        book = self.book_list.search_book_by_title(title)
        if book is None:
            return False
        book.set_publisher(new_publisher)
        return True
    def modify_book_publication_date(self, title, new_publication_date):
        book = self.book_list.search_book_by_title(title)
        if book is None:
            return False
        book.set_publication_date(new_publication_date)
        return True
    def modify_book_number_of_copies(self, title, new_number_of_copies):
        book = self.book_list.search_book_by_title(title)
        if book is None:
            return False
        book.set_number_of_copies(new_number_of_copies)
        return True
    
    def modify_user_firstname(self, username, new_firstname):
        user = self.user_list.search_user_by_username(username)
        if user is None:
            return False
        user.set_firstname(new_firstname)
        return True
    def modify_user_surname(self, username, new_surname):
        user = self.user_list.search_user_by_username(username)
        if user is None:
            return False
        user.set_surname(new_surname)
        return True
    def modify_user_house_number(self, username, new_house_number):
        user = self.user_list.search_user_by_username(username)
        if user is None:
            return False
        user.set_house_number(new_house_number)
        return True
    def modify_user_street_name(self, username, new_street_name):
        user = self.user_list.search_user_by_username(username)
        if user is None:
            return False
        user.set_street_name(new_street_name)
        return True
    def modify_user_postcode(self, username, new_postcode):
        user = self.user_list.search_user_by_username(username)
        if user is None:
            return False
        user.set_postcode(new_postcode)
        return True
    