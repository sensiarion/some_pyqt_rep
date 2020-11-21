import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('./UI.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
