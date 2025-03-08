import sys
from PySide2.QtWidgets import QApplication
from controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create main controller
    controller = MainController()
    controller.start()

    sys.exit(app.exec_())
