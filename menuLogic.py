from gamewindow import GameWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget, QInputDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

nb_players = None
class MenuLogic:
    def __init__(self, ui, MainWindow, diff_mod, player_history):
        self.ui = ui
        self.MainWindow = MainWindow
        self.nb_players = None
        self.player_list = None
        self.diff_mod = diff_mod
        self.player_history = player_history

    def play_alone(self, MainWindow, type_jeu, diff_mod, player_history):
        nb_players = 1
        # Implement logic for one player (IA)
        ok1 = MenuLogic.name_player(self, MainWindow, player_history)
        print(ok1)
        if ok1:
            self.game_window = GameWindow(self, nb_players, type_jeu, self.player_list, MainWindow, diff_mod)
            self.game_window.show()
            self.game_window.resize(900, 900)
            self.game_window.center()
            MainWindow.hide()
        else:
            self.setupUi(MainWindow)
            QMessageBox.warning(MainWindow, "Failed to start game", "Player name input canceled or empty.")
        pass

    def play_two_players(self, MainWindow, type_jeu, diff_mod, player_history):
        nb_players = 2
        ok1, ok2 = MenuLogic.name_players(self, MainWindow, player_history)
        if ok1 and ok2:
            self.game_window = GameWindow(self, nb_players, type_jeu, self.player_list, MainWindow, diff_mod)
            self.game_window.show()
            self.game_window.resize(900, 900)
            self.game_window.center()
            MainWindow.hide()
        else:
            self.setupUi(MainWindow)
            QMessageBox.warning(MainWindow, "Failed to start game", "Player name input canceled or empty.")
            
    def morpion_clicked(self, MainWindow, diff_mod, player_history):
        self.menuDiff.removeAction(self.Diffrand)
        self.menuDiff.removeAction(self.DiffbestMove)
        self.menuOptions.setTitle("Options")
        if diff_mod == 0:
            self.menuDiff.setTitle("Current difficulty - Easy")
        else:
            self.menuDiff.setTitle("Current difficulty - Hard")
        self.vertical_layout.removeWidget(self.morpion_button)
        self.vertical_layout.removeWidget(self.meta_button)
        self.vertical_layout.removeWidget(self.exit_button)
        self.vertical_layout.removeWidget(self.leaderboard_button)

        # Adds the new buttons to the layout
        MenuLogic.change_options_bar(self, MainWindow)
        self.label.setText("1D - Morpion")
        self.singleplayer_button = QtWidgets.QPushButton("Singleplayer", self.centralwidget)
        self.singleplayer_button.setIcon(QtGui.QIcon("icon_singleplayer.png"))
        self.vertical_layout.addWidget(self.singleplayer_button)

        self.two_players_button = QtWidgets.QPushButton("Two Players", self.centralwidget)
        self.two_players_button.setIcon(QtGui.QIcon("icon_two_players.png"))
        self.vertical_layout.addWidget(self.two_players_button)

        self.leaderboard_button = QtWidgets.QPushButton("Leaderboard", self.centralwidget)
        self.leaderboard_button.setIcon(QtGui.QIcon("icon_leaderboard.png"))
        self.vertical_layout.addWidget(self.leaderboard_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        self.vertical_layout.addWidget(self.exit_button)
        
        type_jeu = 1

        # Connects the signals from the added buttons to the desired functions
        self.singleplayer_button.clicked.connect(lambda: MenuLogic.play_alone(self, MainWindow, type_jeu, diff_mod, player_history))
        self.two_players_button.clicked.connect(lambda: MenuLogic.play_two_players(self, MainWindow, type_jeu, diff_mod, player_history))
        self.exit_button.clicked.connect(MainWindow.close)
        self.leaderboard_button.clicked.connect(lambda: self.view_players())

        return None
    
    def meta_morpion_clicked(self, MainWindow, diff_mod, player_history):
        self.menuDiff.removeAction(self.Diffrand)
        self.menuDiff.removeAction(self.DiffbestMove)
        self.menuOptions.setTitle("Options")
        if diff_mod == 0:
            self.menuDiff.setTitle("Current difficulty - Easy")
        else:
            self.menuDiff.setTitle("Current difficulty - Hard")
        self.vertical_layout.removeWidget(self.morpion_button)
        self.vertical_layout.removeWidget(self.meta_button)
        self.vertical_layout.removeWidget(self.exit_button)
        self.vertical_layout.removeWidget(self.leaderboard_button)

        # Adds the new buttons to the layout
        MenuLogic.change_options_bar(self, MainWindow)
        self.label.setText("2D - Meta Morpion")
        self.singleplayer_button = QtWidgets.QPushButton("Singleplayer", self.centralwidget)
        self.singleplayer_button.setIcon(QtGui.QIcon("icon_singleplayer.png"))
        self.vertical_layout.addWidget(self.singleplayer_button)

        self.two_players_button = QtWidgets.QPushButton("Two Players", self.centralwidget)
        self.two_players_button.setIcon(QtGui.QIcon("icon_two_players.png"))
        self.vertical_layout.addWidget(self.two_players_button)

        self.leaderboard_button = QtWidgets.QPushButton("Leaderboard", self.centralwidget)
        self.leaderboard_button.setIcon(QtGui.QIcon("icon_leaderboard.png"))
        self.vertical_layout.addWidget(self.leaderboard_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        self.vertical_layout.addWidget(self.exit_button)
        
        type_jeu = 2

        # Connects the signals from the added buttons to the desired functions
        self.singleplayer_button.clicked.connect(lambda: MenuLogic.play_alone(self, MainWindow, type_jeu, diff_mod, player_history))
        self.two_players_button.clicked.connect(lambda: MenuLogic.play_two_players(self, MainWindow, type_jeu, diff_mod, player_history))
        self.exit_button.clicked.connect(MainWindow.close)
        self.leaderboard_button.clicked.connect(lambda: self.view_players())

        return None
    
    def change_options_bar(self, MainWindow):
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuOptions.addAction(self.actionNew)
        self.actionNew.triggered.connect(lambda: self.setupUi(MainWindow))
        self.actionNew.setText("Back to Main Menu")
        self.actionNew.setShortcut("Ctrl+N")

        return None
    def name_player(self, MainWindow, player_history):
        # Use QInputDialog to get name of one player
        ok1 = False
        text_popup = 'Player history:\n'
        for player in player_history.items():
            text_popup += f'{player}\n'

        dialog = QInputDialog(MainWindow)
        dialog.setLabelText(text_popup)

        choice, ok1 = QInputDialog.getItem(MainWindow, 'Choose a player', 'Select an existing player 1 ?', self.player_history.keys(), 0, False)

        if ok1:
            print(f'Você escolheu jogar com {choice}')
            player1_name = choice
            # Adicione aqui a lógica para iniciar o jogo com o jogador escolhido
        else:
            new_player1, ok1 = QInputDialog.getText(MainWindow, 'New player', "Type the new player's name:")
            if new_player1 == "":
                new_player1 = "Guest1"
            if ok1 and new_player1:
                print(f'Você criou um novo jogador: {new_player1}')
                self.player_history[new_player1] = 0  # Adiciona o novo jogador com score inicial zero
                self.save_players(new_player1, 0)
                player1_name = new_player1
        if ok1:
            # Now we can use player1_name and player2_name as needed
            print(f"Player 1's name: {player1_name}")
            self.player_list = [player1_name, "IA"]
        
        return ok1

    def name_players(self, MainWindow, player_history):
        # Use QInputDialog to get names of two players
        ok1, ok2 = False, False
        text_popup = 'Player history:\n'
        for player in player_history.items():
            text_popup += f'{player}\n'

        dialog = QInputDialog(MainWindow)
        dialog.setLabelText(text_popup)

        choice, ok1 = QInputDialog.getItem(MainWindow, 'Choose a player', 'Select an existing player 1 ?', self.player_history.keys(), 0, False)

        if ok1:
            print(f'Você escolheu jogar com {choice}')
            player1_name = choice
            # Adicione aqui a lógica para iniciar o jogo com o jogador escolhido
        else:
            new_player1, ok1 = QInputDialog.getText(MainWindow, 'New player', "Type the new player's name:")
            if new_player1 == "":
                new_player1 = "Guest1"
            if ok1 and new_player1:
                print(f'Você criou um novo jogador: {new_player1}')
                self.player_history[new_player1] = 0  # Adiciona o novo jogador com score inicial zero
                self.save_players(new_player1, 0)
                player1_name = new_player1
        if ok1:
            text_popup = 'Player history:\n'
            for player in self.player_history.items():
                text_popup += f'{player}\n'
            
            dialog = QInputDialog(MainWindow)
            dialog.setLabelText(text_popup)
            
            choice2, ok2 = QInputDialog.getItem(MainWindow, 'Choose a player 2', 'Select an existing player 2 ?', self.player_history.keys(), 0, False)

        if ok2 and ok1:
            if choice2:
                print(f'Você escolheu jogar com {choice2}')
                player2_name = choice2
        elif ok1:
            new_player2, ok2 = QInputDialog.getText(MainWindow, 'New player', "Type the new player's name:")
            if new_player2 == "":
                new_player2 = "Guest2"
            if ok2 and new_player2:
                print(f'Você criou um novo jogador: {new_player2}')
                self.save_players(new_player2, 0)
                player2_name = new_player2


        # Check if both players provided names
        if ok1 and ok2:
            # Now we can use player1_name and player2_name as needed
            print(f"Player 1's name: {player1_name}")
            print(f"Player 2's name: {player2_name}")
            self.player_list = [player1_name, player2_name]
            return [ok1, ok2]
        else:
            return [False, False]