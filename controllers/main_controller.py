from PySide2.QtWidgets import QMessageBox

from views.main_window import MainWindow
from models.user_model import UserModel, User


class MainController:
    def __init__(self):
        # Instantiate the View and Model
        self.user_model = UserModel()
        self.view = MainWindow()

        # Connect view signals to controller methods
        self.view.btnAdd.clicked.connect(self.add_user)
        self.view.btnDelete.clicked.connect(self.delete_user)

    def start(self):
        """Displays the main window."""
        self.view.show()

    def add_user(self):
        """Gets data from the view, creates a User, and stores it in the model."""
        name = self.view.lineEditName.text()
        age_text = self.view.lineEditAge.text()

        if not name or not age_text.isdigit():
            QMessageBox.warning(self.view, "Error", "Invalid data.")
            return

        age = int(age_text)
        user = User(name, age)
        self.user_model.add_user(user)

        # Update the user list in the view
        self.update_user_list()

    def delete_user(self):
        """Deletes the selected user from the list."""
        index = self.view.userList.currentRow()
        if index < 0:
            QMessageBox.information(self.view, "Info", "No user selected.")
            return
        self.user_model.delete_user(index)
        self.update_user_list()

    def update_user_list(self):
        """Clears and reloads the user list in the view."""
        self.view.userList.clear()
        for user in self.user_model.get_users():
            self.view.userList.addItem(f"{user.name} - {user.age} years old")
