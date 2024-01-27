import sys
import game
import IA
from PyQt5 import QtTest
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QSizePolicy,
    QVBoxLayout,
    QMainWindow,
    QApplication,
    QDesktopWidget,
    QMenuBar,
    QAction,
    QMessageBox
)

from PyQt5.QtCore import Qt


edge_size = 3 # number of squares in an edge of the board

class Board_1D(QWidget):
    def __init__(self, nb_players, player_list, MainWindow, boardcontainer, diff_mod):
        super().__init__()
        self.initUI()
        self.nb_players = nb_players
        self.player_list = player_list
        self.MainWindow = MainWindow
        self.boardcontainer = boardcontainer
        self.diff_mod = diff_mod
        self.player_history = Board_1D.load_players(self)
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setCursor(Qt.SizeAllCursor)
        # Create the matrix to represent the board
        self.list_forbidden_squares = []
        self.last_square = None
        self.table = [[None for i in range(edge_size)] for j in range(edge_size)]  # edge_sizexedge_size space for buttons
        self.square = [[None for i in range(edge_size)] for j in range(edge_size)] # liste of squares
        # Set a fixed size for the buttons and the window
        button_size = 300
        self.setFixedSize(button_size * edge_size, button_size * edge_size)

        # Variable to track the current player (X or O)
        self.current_player = "X"

        # Create the buttons and add them to the matrix
        for i in range(edge_size):
            for j in range(edge_size):
                btn = QPushButton("", self)
                btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                btn.setFixedSize(button_size, button_size)
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                grid.addWidget(btn, i, j)
                self.table[i][j] = btn

                # Increase the font size for larger buttons
                self.update_font_size(btn)


        self.setWindowTitle("Morpion")
        self.show()

    def resizeEvent(self, event):
        # Override the resizeEvent method to handle window resize
        for i in range(edge_size):
            for j in range(edge_size):
                btn = self.table[i][j]
                self.update_font_size(btn)

    def update_font_size(self, button, times=1):
        # Update font size based on window width
        font_size = times * self.width() // 7
        font = button.font()
        font.setPointSize(font_size)
        button.setFont(font)

    def get_player_color(self):
        # Return color based on the current player
        return "red" if self.current_player == "X" else "blue"

    def get_block_color(self, row, col):
        # Return alternating colors for the blocks
        return "lightgray" if (row + col) % 2 == 0 else "gray"

    
    def disable_buttons(self): 
        # Disable the buttons in the list of forbidden squares
        for row, col in self.list_forbidden_squares:
            self.table[row][col].setEnabled(False)

    def enable_all_buttons(self): 
        for row in range(edge_size):
            for col in range(edge_size):
                self.table[row][col].setEnabled(True)

    def disable_all_buttons(self):
        for row in range(edge_size):
            for col in range(edge_size):
                self.table[row][col].setEnabled(False)
   
    
    def possible_moves(self): # returns the list of all the possible moves 
        return ([(row, col) for row in range(edge_size) for col in range(edge_size) 
                 if not ((row, col) in self.list_forbidden_squares)])

    

    def button_click(self, row, col, is_player=True): 
        # Function to be called as the button is clicked
        list_possible_moves = self.possible_moves()
        print(list_possible_moves)
        if (row, col) in list_possible_moves: # Check if the button is empty
            self.table[row][col].setText(self.current_player)
            self.table[row][col].setStyleSheet(f"background-color: {self.get_player_color()}")
            self.square[row][col]=self.current_player
            # Disable buttons associated with forbidden squares
            self.list_forbidden_squares.append((row,col))

            # Toggle player
            self.last_square = (row,col)

            if game.is_winner(self.square,self.current_player):# Check if the game is over
                print("win")
                self.disable_all_buttons()
                print(self.current_player)  
                self.show_winner_message()
                Board_1D.update_score(self.current_player, self.player_history)
            if len(self.list_forbidden_squares)==edge_size**2 :
                print("égalité")
                self.show_egalite_message()
            list_possible_moves = self.possible_moves() # Update the list of possible moves for next turn
            print(list_possible_moves)
            print(self.list_forbidden_squares)
            # Modifies the cursor depending on the current player (stop for 'O', + for 'X')
            if self.current_player == "O": 
                self.setCursor(Qt.SizeAllCursor)
            else:
                self.setCursor(Qt.ForbiddenCursor)
            self.current_player = "O" if self.current_player == "X" else "X" #End of the turn, make the other player the current one
        # Make the AI play if necessary
        if (self.nb_players == 1 and is_player and 
            not game.is_winner(self.square, "X") and 
                len(self.list_forbidden_squares) != edge_size**2):
            self.disable_all_buttons()
            QtTest.QTest.qWait(1000)
            if self.diff_mod == 1: # Difficulty : Hard
                row, col = IA.find_best_move_1D(self.square, list_possible_moves)            
            elif self.diff_mod == 0: # Difficulty : Easy
                row, col = IA.IA_random(self.square,list_possible_moves)
            
            self.table[row][col].setText(self.current_player)
            self.table[row][col].setStyleSheet(f"background-color: {self.get_player_color()}")
            # Enable buttons after the waiting time
            self.enable_all_buttons()
            self.disable_buttons()
            self.button_click(row, col, is_player = False)

    def show_winner_message(self):
        if self.current_player == "X":
            self.current_player = self.player_list[0]
        else:
            self.current_player = self.player_list[1]
        winner_message = QMessageBox()
        winner_message.setWindowTitle("Game Over")
        winner_message.setText(f"Player {self.current_player} won!")

        back_to_menu_button = winner_message.addButton("Back to Menu", QMessageBox.ActionRole)
        exit_button = winner_message.addButton("Exit Game", QMessageBox.RejectRole)

        winner_message.exec_()

        if winner_message.clickedButton() == back_to_menu_button:
            self.MainWindow.show()
            self.boardcontainer.close()
        elif winner_message.clickedButton() == exit_button:
            self.boardcontainer.close()

    def show_egalite_message(self):
        egalite_message = QMessageBox()
        egalite_message.setWindowTitle("Game Over")
        egalite_message.setText(f"No player has won! It's a draw")

        back_to_menu_button = egalite_message.addButton("Back to Main Menu", QMessageBox.ActionRole)
        exit_button = egalite_message.addButton("Exit Game", QMessageBox.RejectRole)

        egalite_message.exec_()

        if egalite_message.clickedButton() == back_to_menu_button:
            self.MainWindow.show()
            self.boardcontainer.close()
        elif egalite_message.clickedButton() == exit_button:
            self.boardcontainer.close()

    def load_players(self):
        try:
            with open('players.txt', 'r') as file:
                lines = file.readlines()
                players = {}
                for linha in lines:
                    player, score = linha.strip().split(':')
                    players[player] = int(score)
                return players
        except FileNotFoundError:
            return {}
        
    def update_score(player, player_history):
        if player in player_history:
            player_history[player] += 1
        else:
            pass

        with open('players.txt', 'w') as file:
            for player, score in player_history.items():
                file.write(f'{player}:{score}\n')
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Board_1D(nb_players=1)
    sys.exit(app.exec_())