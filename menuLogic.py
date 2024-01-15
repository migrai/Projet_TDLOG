from gamewindow import GameWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget, QInputDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

nb_players = None
class MenuLogic:
    def __init__(self, ui, MainWindow):
        self.ui = ui
        self.MainWindow = MainWindow
        self.nb_players = None

    def play_alone(self, MainWindow):
        nb_players = 1
        # Implement logic for one player (IA)
        ok1 = MenuLogic.name_player(self, MainWindow)
        print(ok1)
        if ok1:
            self.game_window = GameWindow(self)
            self.game_window.show()
            self.game_window.resize(900, 900)
            self.game_window.center()
            MainWindow.close()
        else:
            self.setupUi(MainWindow)
            QMessageBox.warning(MainWindow, "Failed to start game", "Player name input canceled or empty.")
        pass

    def play_two_players(self, MainWindow):
        nb_players = 2
        ok1, ok2 = MenuLogic.name_players(self, MainWindow)
        print(ok1, ok2)
        if ok1 and ok2:
            self.game_window = GameWindow(self)
            self.game_window.show()
            self.game_window.resize(900, 900)
            self.game_window.center()
            MainWindow.close()
        else:
            self.setupUi(MainWindow)
            QMessageBox.warning(MainWindow, "Failed to start game", "Player name input canceled or empty.")
            
    def morpion_clicked(self, MainWindow):
        
        self.vertical_layout.removeWidget(self.morpion_button)
        self.vertical_layout.removeWidget(self.meta_button)
        self.vertical_layout.removeWidget(self.exit_button)

        # Adds the new buttons to the layout
        MenuLogic.change_options_bar(self, MainWindow)
        self.label.setText("1D - Morpion")
        self.singleplayer_button = QtWidgets.QPushButton("Singleplayer", self.centralwidget)
        self.singleplayer_button.setIcon(QtGui.QIcon("icon_singleplayer.png"))
        self.vertical_layout.addWidget(self.singleplayer_button)

        self.two_players_button = QtWidgets.QPushButton("Two Players", self.centralwidget)
        self.two_players_button.setIcon(QtGui.QIcon("icon_two_players.png"))
        self.vertical_layout.addWidget(self.two_players_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        self.vertical_layout.addWidget(self.exit_button)

        # Connects the signals from the added buttons to the desired functions
        self.singleplayer_button.clicked.connect(lambda: MenuLogic.play_alone(self, MainWindow))
        self.two_players_button.clicked.connect(lambda: MenuLogic.play_two_players(self, MainWindow))
        self.exit_button.clicked.connect(MainWindow.close)

        return None
    
    def meta_morpion_clicked(self, MainWindow):
        
        self.vertical_layout.removeWidget(self.morpion_button)
        self.vertical_layout.removeWidget(self.meta_button)
        self.vertical_layout.removeWidget(self.exit_button)

        # Adds the new buttons to the layout
        MenuLogic.change_options_bar(self, MainWindow)
        self.label.setText("2D - Meta Morpion")
        self.singleplayer_button = QtWidgets.QPushButton("Singleplayer", self.centralwidget)
        self.singleplayer_button.setIcon(QtGui.QIcon("icon_singleplayer.png"))
        self.vertical_layout.addWidget(self.singleplayer_button)

        self.two_players_button = QtWidgets.QPushButton("Two Players", self.centralwidget)
        self.two_players_button.setIcon(QtGui.QIcon("icon_two_players.png"))
        self.vertical_layout.addWidget(self.two_players_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        self.vertical_layout.addWidget(self.exit_button)

        # Connects the signals from the added buttons to the desired functions
        self.singleplayer_button.clicked.connect(lambda: MenuLogic.play_alone(self, MainWindow))
        self.two_players_button.clicked.connect(lambda: MenuLogic.play_two_players(self, MainWindow))
        self.exit_button.clicked.connect(MainWindow.close)

        return None
    
    def change_options_bar(self, MainWindow):
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuOptions.addAction(self.actionNew)
        self.actionNew.triggered.connect(lambda: self.setupUi(MainWindow))
        self.actionNew.setText("Back to Main Menu")
        self.actionNew.setShortcut("Ctrl+N")
        return None
    def name_player(self, MainWindow):
        # Use QInputDialog to get names of two players
        player1_name, ok1 = QInputDialog.getText(MainWindow, "Player 1 Name", "Enter Player 1's Name:")
        # Check if the player provided their name
        if ok1:
            # Now we can use player1_name and player2_name as needed
            print(f"Player 1's name: {player1_name}")
        return ok1

    def name_players(self, MainWindow):
        # Use QInputDialog to get names of two players
        player1_name, ok1 = QInputDialog.getText(MainWindow, "Player 1 Name", "Enter Player 1's Name:")
        player2_name, ok2 = QInputDialog.getText(MainWindow, "Player 2 Name", "Enter Player 2's Name:")

        # Check if both players provided names
        if ok1 and ok2:
            # Now we can use player1_name and player2_name as needed
            print(f"Player 1's name: {player1_name}")
            print(f"Player 2's name: {player2_name}")

        return [ok1, ok2]
