import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QPushButton, QWidget, QDesktopWidget
from board import GameWindow


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Vertical button layout
        layout = QVBoxLayout()

        # Button to play alone
        play_alone_button = QPushButton('Singleplayer', self)
        play_alone_button.clicked.connect(self.play_alone)
        play_alone_button.setStyleSheet("background-color: blue; color: white; border: 1px solid black;")
        layout.addWidget(play_alone_button)

        # Button for two players
        play_two_players_button = QPushButton('Two Players', self)
        play_two_players_button.clicked.connect(self.play_two_players)
        play_two_players_button.setStyleSheet("background-color: green; color: white; border: 1px solid black;")
        layout.addWidget(play_two_players_button)

        # Button to exit
        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)
        exit_button.setStyleSheet("background-color: red; color: white; border: 1px solid black;")
        layout.addWidget(exit_button)

        central_widget.setLayout(layout)

        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Game Menu')
        self.center()

    def center(self):
        # Centers window
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def play_alone(self):
        # Implement logic for one player (IA)
        pass

    def play_two_players(self):
        self.game_window = GameWindow()
        self.game_window.show()
        self.game_window.resize(900, 900)
        self.game_window.center()
        self.hide()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(app.exec_())