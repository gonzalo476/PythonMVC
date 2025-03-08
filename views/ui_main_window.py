# views/ui_main_window.py
# This code is generated with pyside2-uic or pyuic5 from your .ui
from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Main Window")
        MainWindow.setFixedSize(220, 280)

        # Simple example of widgets
        self.lineEditName = QLineEdit(MainWindow)
        self.lineEditName.setGeometry(10, 10, 200, 30)

        self.lineEditAge = QLineEdit(MainWindow)
        self.lineEditAge.setGeometry(10, 50, 200, 30)

        self.btnAdd = QPushButton("Add User", MainWindow)
        self.btnAdd.setGeometry(10, 90, 200, 30)

        self.userList = QListWidget(MainWindow)
        self.userList.setGeometry(10, 130, 200, 100)

        self.btnDelete = QPushButton("Delete User", MainWindow)
        self.btnDelete.setGeometry(10, 240, 200, 30)
