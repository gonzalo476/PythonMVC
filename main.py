import sys
from PySide2.QtWidgets import QApplication
from app.models.user_model import User
from app.views.user_view import UserView
from app.controllers.user_controller import UserController
from app.db.database import Database


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Set up the MVC components
    db = Database()
    view = UserView()
    controller = UserController(db, view)

    # Show the view
    view.show()

    # Run the application
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
