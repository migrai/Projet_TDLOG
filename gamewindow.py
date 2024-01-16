from board import *
from board_1D import Board_1D
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon

class GameWindow(QMainWindow):
    def __init__(self, ui, nb_players, type_jeu, player_list, MainWindow):
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

        if type_jeu == 2:
            self.central_widget = Board(nb_players, player_list, MainWindow, self)
        else:
            self.central_widget = Board_1D(nb_players, player_list, MainWindow, self)

        # Set the layout for the main window
        main_layout = QVBoxLayout()
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