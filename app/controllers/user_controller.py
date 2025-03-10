from app.models.user_model import User


class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connect view signals to controller methods
        self.view.user_added.connect(self.add_user)
        self.view.user_updated.connect(self.update_user)
        self.view.user_deleted.connect(self.delete_user)

        # Initial display of users
        self.refresh_user_list()

    def add_user(self, name, email, phone):
        user = User(None, name, email, phone)
        user_id = self.model.add_user(user)
        self.refresh_user_list()
        self.view.show_success(f"User added with ID:  {user_id}")

    def update_user(self, user_id, name, email, phone):
        user = User(user_id, name, email, phone)
        success = self.model.update_user(user)

        if success:
            self.refresh_user_list()
            self.view.show_success(f"User with ID {user_id} updated successfully")
        else:
            self.view.show_error(f"Failed to update user with ID: {user_id}")

    def delete_user(self, user_id):
        success = self.model.delete_user(user_id)
        if success:
            self.refresh_user_list()
            self.view.show_success(f"User with ID {user_id} deleted successfully")
        else:
            self.view.show_error(f"Failed to delete user with ID: {user_id}")

    def refresh_user_list(self):
        users = self.model.get_all_users()
        self.view.display_users(users)
