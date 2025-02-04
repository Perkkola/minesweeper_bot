import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,  QSize
from PyQt6.QtGui import QIcon
from minesweeper import Game
import numpy as np

class CustomButton(QPushButton):
    def __init__(self, text, main_window):
        super().__init__(text)
        self.main_window = main_window

    def mousePressEvent(self, event):
        btn = event.button()
        if btn == Qt.MouseButton.RightButton and self.isEnabled():
            x = self.property("position")[0]
            y = self.property("position")[1]

            if self.property("flag_toggled"):
                self.setIcon(QIcon())
                self.setProperty("flag_toggled", False)
                self.main_window.game.game[x][y].flagged = False
            else:
                self.setProperty("flag_toggled", True)
                self.setIcon(QIcon("./Minesweeper_flag.svg.png"))
                self.main_window.game.game[x][y].flagged = True
        else:
            super().mousePressEvent(event)

class MainWindow(QMainWindow):
    
    def __init__(self, window_height, window_width, game):
        super().__init__()
        self.window_height = window_height
        self.window_width = window_width
        self.buttons = np.empty((window_width, window_height), dtype=QWidget)
        self.game = game
        self.colors = {
            1: "#0000FF",
            2: "#007B00",
            3: "#FF0000",
            4: "#00007B",
            5: "#7B0000",
            6: "#007B7B",
            7: "#000000",
            8: "#7B7B7B"
            }
        
        
        
        self.setWindowTitle("Minesweeper GUI")
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)


        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet(f"background-color: grey")
        self.reset_button.clicked.connect(self.reset)
        self.reset_button.setFixedSize(16*self.window_height, 20)
        layout.addWidget(self.reset_button)

        game_layout = QGridLayout()
        game_layout.setContentsMargins(0,0,0,0)
        game_layout.setSpacing(0)

        for i in range(self.window_width):
            for j in range(self.window_height):
                btn = CustomButton("", self)
                btn.setStyleSheet(f"background-color: lightgrey")
                btn.setFixedSize(16, 16)
                btn.setProperty("position", (i, j))
                btn.setProperty("flag_toggled", False)
                btn.clicked.connect(self.button_clicked)

                self.buttons[i][j] = btn
                game_layout.addWidget(btn, i, j)

        layout.addLayout(game_layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setFixedSize(16*self.window_height, 16*self.window_width + 20)
        self.setCentralWidget(widget)

    def button_clicked(self):
        sender = self.sender()
        if sender.property("flag_toggled"): return
        sender.setEnabled(False)
        pos = sender.property("position")

        revealed = self.game.reveal_tile(pos[0], pos[1])
        if self.game.lost: self.disable_all()
        if self.game.won:
            self.disable_all()
            self.reset_button.setText("You Won! Reset")

        self.update_buttons(revealed)

    def update_buttons(self, revealed):
        for el in revealed:
            btn = self.buttons[el[0]][el[1]]
            btn.setEnabled(False)
            btn.setStyleSheet(f"background-color: #BDBDBD")
            btn.setStyleSheet(f"color: #BDBDBD")

            if el[2] == 0: continue
            if el[2] == 9:
                btn.setStyleSheet(f"background-color: black")
                continue
                    
            btn.setText(str(el[2]))
            btn.setStyleSheet(f"color: {self.colors[el[2]]}")
    
    def disable_all(self):
        for i in range(self.window_width):
            for j in range(self.window_height):
                self.buttons[i][j].setEnabled(False)
    
    def reset(self):
        self.game.started = False
        self.game.lost = False
        self.game.won = False
        self.reset_button.setText("Reset")
        for i in range(self.window_width):
            for j in range(self.window_height):
                btn = self.buttons[i][j]
                btn.setEnabled(True)
                btn.setProperty("flag_toggled", False)
                self.game.game[i][j].flagged = False
                btn.setIcon(QIcon())
                btn.setStyleSheet(f"background-color: lightgrey")
                btn.setText("")

app = QApplication(sys.argv)
args = sys.argv
if len(args) < 4:
    print("Please provie width, height and the amount of bombs, in that order.")
    exit()

if int(args[3]) >= int(args[1])*int(args[2]):
    print("Idiot")
    exit()

game = Game(int(args[1]), int(args[2]), int(args[3]) )

window = MainWindow(int(args[1]), int(args[2]), game)
window.show()

app.exec()