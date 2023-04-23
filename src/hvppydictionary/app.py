import sys

from PySide6.QtWidgets import QApplication

from hvppydictionary.mainwindow import MainWindow


def main():
    """Main function of the application."""
    # Create the application object.
    app = QApplication(sys.argv)

    # Create the main window.
    window = MainWindow()

    # Show the window.
    window.show()

    # Run the application.
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()