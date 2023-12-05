from board import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget
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

        self.central_widget = Board()
        self.setCentralWidget(self.central_widget)

        self.setGeometry(900, 900, 900, 900)
        self.setWindowTitle('Meta-Morpion')

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