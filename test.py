import users_list
from user import User

users_list = users_list.UsersList()
user1 = User("user1", "John", "Doe", "1", "High Street", "AB12 3CD", "sdfsdf@gmail.com", "01/01/2000")
users_list.add_user(user1)

user2 = User("user2", "Jane", "Smith", "2", "Main Street", "EF34 5GH", "sd@gmail.com", "01/01/2000")
users_list.add_user(user2)

print(users_list.search_user_by_username("user2"))  # Expected output: John