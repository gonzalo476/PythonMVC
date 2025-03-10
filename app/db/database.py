from app.models.user_model import User


class Database:
    def __init__(self):
        # In-memory database for simplicity
        self.users = {}
        self.last_id = 0

        # Add some sample data
        self.add_user(User(None, "John Doe", "john@example.com", "555-1234"))
        self.add_user(User(None, "Jane Smith", "jane@example.com", "555-5678"))

    def add_user(self, user):
        self.last_id += 1
        user.id = self.last_id
        self.users[user.id] = user
        return user.id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return list(self.users.values())

    def update_user(self, user):
        if user.id in self.users:
            self.users[user.id] = user
            return True
        return False

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
