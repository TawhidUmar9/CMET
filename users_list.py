class UsersList:
    ## This class is used to store the list of users in a dictionary. Key is the username and value is the user object
    def __init__(self):
        self.users = {}
    
    def add_user(self, user):
        if user.username in self.users:
            return False
        self.users[user.username] = user
        return True  # Return True when user is successfully added
    
    def remove_user(self, firstname):
        if not firstname:
            return False
        target_user = [user for user in self.users.values() if user.firstname == firstname]
        if not target_user:
            return False
        if len(target_user) > 1:
            print("Multiple users found with the same first name")
            return False
        # Remove the user from the dictionary
        del self.users[target_user[0].username]
        return True
    
    def search_user_by_username(self, username):
        if not username:
            return None
        return self.users.get(username, None)
    
    def modify_user_firstname(self, username, new_firstname):
        user = self.search_user_by_username(username)
        if user is None:
            return False
        user.set_firstname(new_firstname)
        return True
    def modify_user_surname(self, username, new_surname):
        user = self.search_user_by_username(username)
        if user is None:
            return False
        user.set_surname(new_surname)
        return True
    def modify_user_house_number(self, username, new_house_number):
        user = self.search_user_by_username(username)
        if user is None:
            return False
        user.set_house_number(new_house_number)
        return True
    def modify_user_street_name(self, username, new_street_name):
        user = self.search_user_by_username(username)
        if user is None:
            return False
        user.set_street_name(new_street_name)
        return True
    def modify_user_postcode(self, username, new_postcode):
        user = self.search_user_by_username(username)
        if user is None:
            return False
        user.set_postcode(new_postcode)
        return True
    def get_user_count(self):
        # Return the number of users in the dictionary
        return len(self.users)