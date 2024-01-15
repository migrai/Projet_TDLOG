from board import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon

class GameWindow(QMainWindow):
    def __init__(self, ui):
        super().__init__()

        self.ui = ui

        # Adds a side menu to the middle of the match

        match_menu_bar = self.menuBar()
        match_menu = match_menu_bar.addMenu('Match')

        # Adds actions to said menu

        exit_action_match = QAction('Exit', self)
        exit_action_match.triggered.connect(self.close)
        match_menu.addAction(exit_action_match)
        return_to_main_menu = QAction('Return to main menu', self)
        return_to_main_menu.triggered.connect(lambda: self.show_main_menu(ui))
        match_menu.addAction(return_to_main_menu)

        # Set up the scoreboard
        self.scoreboard = Scoreboard()

        self.central_widget = Board()

        # Set the layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scoreboard)
        main_layout.addWidget(self.central_widget)
        central_widget_container = QWidget()
        central_widget_container.setLayout(main_layout)
        self.setCentralWidget(central_widget_container)

        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Meta-Morpion')

        self.center()

    def show_main_menu(self, MainWindow):
        original_geometry = MainWindow.save_geometry()
        self.close()
        MainWindow.setupUi(self)
        self.setGeometry(original_geometry)
        self.setCentralWidget(MainWindow.centralwidget)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Scoreboard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.score_label = QLabel('Score: 0', self)
        self.game_label = QLabel('Game Status', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.score_label, alignment=Qt.AlignTop | Qt.AlignRight)
        vbox.addWidget(self.game_label, alignment=Qt.AlignTop | Qt.AlignRight)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def update_score(self, score):
        self.score_label.setText(f'Score: {score}')

    def update_game_label(self, text):
        self.game_label.setText(text)