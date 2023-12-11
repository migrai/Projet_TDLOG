from gamewindow import GameWindow

class MenuLogic:
    def __init__(self, ui, MainWindow):
        self.ui = ui
        self.MainWindow = MainWindow

    def play_alone(self):
        # Implement logic for one player (IA)
        pass

    def play_two_players(self, MainWindow):
        self.game_window = GameWindow(self)
        self.game_window.show()
        self.game_window.resize(900, 900)
        self.game_window.center()
        MainWindow.hide()