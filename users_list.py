class UsersList:
    ## This class is used to store the list of users
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