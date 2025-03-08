class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserModel:
    """Model that manages the user list"""

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_users(self):
        return self.users

    def delete_user(self, index):
        if 0 <= index < len(self.users):
            del self.users[index]
