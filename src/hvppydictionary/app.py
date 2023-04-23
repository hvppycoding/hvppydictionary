import sys

from PySide6.QtWidgets import QApplication, QMainWindow


def main():
    """Main function of the application."""
    # Create the application object.
    app = QApplication(sys.argv)

    # Create the main window.
    window = QMainWindow()

    # Show the window.
    window.show()

    # Run the application.
    sys.exit(app.exec_())