from PySide2.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)
from PySide2.QtCore import Qt, Signal


class UserView(QMainWindow):
    # Define signals
    user_added = Signal(str, str, str)
    user_updated = Signal(int, str, str, str)
    user_deleted = Signal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Management System")
        self.setMinimumSize(800, 500)

        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Form area
        form_layout = QVBoxLayout()

        # Input fields
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()

        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.phone_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add User")
        self.update_button = QPushButton("Update User")
        self.delete_button = QPushButton("Delete User")
        self.clear_button = QPushButton("Clear Form")

        # Initially disable update and delete buttons
        self.update_button.setEnabled(False)
        self.delete_button.setEnabled(False)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_button)

        form_layout.addLayout(button_layout)
        main_layout.addLayout(form_layout)

        # Table view for users
        self.user_table = QTableWidget(0, 4)
        self.user_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Phone"])
        self.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.user_table)

        # Connect signals to slots
        self.add_button.clicked.connect(self.add_user_clicked)
        self.update_button.clicked.connect(self.update_user_clicked)
        self.delete_button.clicked.connect(self.delete_user_clicked)
        self.clear_button.clicked.connect(self.clear_form)
        self.user_table.itemClicked.connect(self.select_user)

        # Store currently selected user ID
        self.selected_user_id = None

    def add_user_clicked(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and email:
            self.user_added.emit(name, email, phone)
            self.clear_form()
        else:
            QMessageBox.warning(
                self, "Validation Error", "Name and Email are required fields."
            )

    def update_user_clicked(self):
        if self.selected_user_id is None:
            return

        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and email:  # Basic validation
            self.user_updated.emit(self.selected_user_id, name, email, phone)
            self.clear_form()
        else:
            QMessageBox.warning(
                self, "Validation Error", "Name and Email are required fields."
            )

    def delete_user_clicked(self):
        if self.selected_user_id is None:
            return

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete the selected user?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.user_deleted.emit(self.selected_user_id)
            self.clear_form()

    def select_user(self, item):
        row = item.row()
        self.selected_user_id = int(self.user_table.item(row, 0).text())

        # Fill the form with the selected user's data
        self.name_input.setText(self.user_table.item(row, 1).text())
        self.email_input.setText(self.user_table.item(row, 2).text())
        self.phone_input.setText(self.user_table.item(row, 3).text())

        # Enable update and delete buttons
        self.update_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        self.add_button.setEnabled(True)

    def clear_form(self):
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.selected_user_id = None
        self.update_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        self.add_button.setEnabled(True)

    def display_users(self, users):
        self.user_table.setRowCount(0)

        for row, user in enumerate(users):
            self.user_table.insertRow(row)
            self.user_table.setItem(row, 0, QTableWidgetItem(str(user.id)))
            self.user_table.setItem(row, 1, QTableWidgetItem(user.name))
            self.user_table.setItem(row, 2, QTableWidgetItem(user.email))
            self.user_table.setItem(row, 3, QTableWidgetItem(user.phone))

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def show_success(self, message):
        QMessageBox.information(self, "Success", message)
