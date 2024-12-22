import datetime

class User:
    ## username: string
    ## firstname: string
    ## surname: string
    ## house_number: string
    ## street_name: string
    ## post_code: string
    ## email_address: string
    ## date_of_birth: date
    
    def __init__(self, username, firstname, surname, house_number, street_name, post_code, email_address, date_of_birth):
        self.set_username(username)
        self.set_firstname(firstname)
        self.set_surname(surname)
        self.set_house_number(house_number)
        self.set_street_name(street_name)
        self.set_post_code(post_code)
        self.set_email_address(email_address)
        self.set_date_of_birth(date_of_birth)

    def set_username(self, username):
        self._validate_non_empty_string(username, "Username", 50)
        self.username = username
    
    def set_firstname(self, firstname):
        self._validate_non_empty_string(firstname, "Firstname", 50)
        self.firstname = firstname
    
    def set_surname(self, surname):
        self._validate_non_empty_string(surname, "Surname", 50)
        self.surname = surname
    
    def set_house_number(self, house_number):
        self._validate_non_empty_string(house_number, "House number", 10)
        self.house_number = house_number
    
    def set_street_name(self, street_name):
        self._validate_non_empty_string(street_name, "Street name", 100)
        self.street_name = street_name
    
    def set_post_code(self, post_code):
        self._validate_non_empty_string(post_code, "Post code", 10)
        self.post_code = post_code
    
    def set_email_address(self, email_address):
        if not email_address:
            raise ValueError("Email address cannot be empty")
        if len(email_address) > 100:
            raise ValueError("Email address cannot be longer than 100 characters")
        if email_address.count("@") != 1 or email_address.count(".") == 0:
            raise ValueError("Invalid email address")
        self.email_address = email_address
    
    def set_date_of_birth(self, date_of_birth):
        if date_of_birth > datetime.datetime.now().date():
            raise ValueError("Date of birth cannot be in the future")
        self.date_of_birth = date_of_birth

    def _validate_non_empty_string(self, value, field_name, max_length):
        if not value:
            raise ValueError(f"{field_name} cannot be empty")
        if len(value) > max_length:
            raise ValueError(f"{field_name} cannot be longer than {max_length} characters")
    
    def get_username(self): return self.username
    def get_firstname(self): return self.firstname
    def get_surname(self): return self.surname
    def get_house_number(self): return self.house_number
    def get_street_name(self): return self.street_name
    def get_post_code(self): return self.post_code
    def get_email_address(self): return self.email_address
    def get_date_of_birth(self): return self.date_of_birth
    
    def __str__(self):
        return (f"Username: {self.username}, Firstname: {self.firstname}, Surname: {self.surname}, "
                f"House number: {self.house_number}, Street name: {self.street_name}, "
                f"Post code: {self.post_code}, Email address: {self.email_address}, "
                f"Date of birth: {self.date_of_birth}")