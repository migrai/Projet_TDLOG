import sys
import game
import IA
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

class Board_1D(QWidget):
    def __init__(self,nb_players,player_list, MainWindow, boardcontainer):
        super().__init__()
        self.initUI()
        self.nb_players = nb_players
        self.player_list = player_list
        self.MainWindow = MainWindow
        self.boardcontainer = boardcontainer

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setCursor(Qt.SizeAllCursor)
        # Create the matrix to represent the board
        self.list_forbidden_squares = []
        self.last_square = None
        self.table = [[None for i in range(3)] for j in range(3)]  # 3x3 space for buttons
        self.square = [[None for i in range(3)] for j in range(3)] #liste des cases 
        # Set a fixed size for the buttons and the window
        button_size = 300
        self.setFixedSize(button_size * 3, button_size * 3)

        # Variable to track the current player (X or O)
        self.current_player = "X"

        # Create the buttons and add them to the matrix
        for i in range(3):
            for j in range(3):
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
        for i in range(3):
            for j in range(3):
                btn = self.table[i][j]
                self.update_font_size(btn)

    def update_font_size(self, button, times = 1): #fonction qui s
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
        # Désactive les boutons aux coordonnées spécifiées
        for row, col in self.list_forbidden_squares:
            self.table[row][col].setEnabled(False)

    def enable_all_buttons(self):#active tous les boutons 
        for row in range(3):
            for col in range(3):
                self.table[row][col].setEnabled(True)

    def disable_all_buttons(self):#active tous les boutons 
        for row in range(3):
            for col in range(3):
                self.table[row][col].setEnabled(False)
   
    
    def possible_moves(self): # retourne tous les coups possibles 
        return ([(row,col) for row in range(3) for col in range(3) if not ((row, col) in self.list_forbidden_squares) ])

    

    def button_click(self, row, col, is_player = True): 
        # Function to be called as the button is clicked
        #if 
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

            if game.is_winner(self.square,self.current_player):#vérifie si le jeu est fini 
                print("win")
                self.disable_all_buttons()
                print(self.current_player)  
                self.show_winner_message()
            if len(self.list_forbidden_squares)==9 :
                print("égalité")
                self.show_egalite_message()
            list_possible_moves = self.possible_moves() #on modifie la liste des coups possibles pour le tour suivant
            print(list_possible_moves)
            print(self.list_forbidden_squares)
            
            if self.current_player == "O": # modifie le curseur pour indiquer quel joueur doit jouer (un 0 pour le joueur O et un + pour le joueur X)
                self.setCursor(Qt.SizeAllCursor)
            else:
                self.setCursor(Qt.ForbiddenCursor)
            self.current_player = "O" if self.current_player == "X" else "X" #fin du tour, donne la main au joueur suivant
        if self.nb_players == 1 and is_player and not game.is_winner(self.square,"X")and len(self.list_forbidden_squares)!=9 :
            row, col = IA.find_best_move(self.square, list_possible_moves)
            
            self.table[row][col].setText(self.current_player)
            self.table[row][col].setStyleSheet(f"background-color: {self.get_player_color()}")
            self.button_click(row, col, is_player = False)

    def show_winner_message(self):
        if self.current_player == "X":
            self.current_player = self.player_list[0]
        else:
            self.current_player = self.player_list[1]
        winner_message = QMessageBox()
        winner_message.setWindowTitle("Game Over")
        winner_message.setText(f"Player {self.current_player} won!")

        back_to_menu_button = winner_message.addButton("Back to Main Menu", QMessageBox.ActionRole)
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
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Board_1D(nb_players = 1)
    sys.exit(app.exec_())