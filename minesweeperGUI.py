import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, window_height, window_width):
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width
        self.button_is_checked = True

        self.setWindowTitle("Minesweeper")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setFixedSize(QSize(self.window_height, self.window_width))

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)
args = sys.argv
window = MainWindow(int(args[1]), int(args[2]))
window.show()

app.exec()