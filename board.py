import sys
import game
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
)

from PyQt5.QtCore import Qt

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setCursor(Qt.SizeAllCursor)
        # Create the matrix to represent the board
        self.table = [[None] * 9 for _ in range(9)]
        self.list_forbidden_squares = []
        self.last_square = None
        self.big_square_table = [[None for i in range(3)] for j in range(3)]  # 3x3 of big squares
        self.nbr_square_in_big_square = [[0 for i in range(3)] for j in range(3)]
        # Set a fixed size for the buttons and the window
        button_size = 100
        self.setFixedSize(button_size * 9, button_size * 9)

        # Variable to track the current player (X or O)
        self.current_player = "X"

        # Create the buttons and add them to the matrix
        for i in range(9):
            for j in range(9):
                btn = QPushButton("", self)
                btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                btn.setFixedSize(button_size, button_size)
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                grid.addWidget(btn, i, j)
                self.table[i][j] = btn

                # Increase the font size for larger buttons
                self.update_font_size(btn)

                # Set background color based on the block position
                block_color = self.get_block_color(i // 3, j // 3)
                btn.setStyleSheet(
                    f"background-color: {block_color}; border: 1px solid black"
                )

        self.setWindowTitle("Meta-Morpion")
        self.show()

    def resizeEvent(self, event):
        # Override the resizeEvent method to handle window resize
        for i in range(9):
            for j in range(9):
                btn = self.table[i][j]
                self.update_font_size(btn)

    def update_font_size(self, button, times = 1): #fonction qui s
        # Update font size based on window width
        font_size = times * self.width() // 20
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
        for row in range(9):
            for col in range(9):
                self.table[row][col].setEnabled(True)

    def disable_all_buttons(self): # rend inactif tous les boutons
        for row in range(9):
            for col in range(9):
                self.table[row][col].setEnabled(False)    
    
    def possible_moves(self): # retourne tous les coups possibles 
        return ([(row,col) for row in range(9) for col in range(9) if not ((row, col) in self.list_forbidden_squares or (row,col) in game.forbidden_moves_for_current_player(self.last_square,self.big_square_table)) ])

    def create_big_button(self,x,y) : #créé la grosse case au point (x,y)
        button_size = 293
        grid = self.layout()
        btn = QPushButton("", self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.setFixedSize(button_size, button_size)
        grid.addWidget(btn, x*3 , 3*y)
        # Increase the font size for larger buttons
        self.update_font_size(btn,times = 3)

        # Set background color based on the block position
        block_color = self.get_player_color()
        btn.setStyleSheet(f"background-color: {block_color}; border: 1px solid black")
        btn.setText(self.current_player)

    def color_pat_big_square(self,x,y):
        button_size = 293
        grid = self.layout()
        btn = QPushButton("", self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.setFixedSize(button_size, button_size)
        grid.addWidget(btn, x*3 , 3*y)
        btn.setStyleSheet(f"background-color: {'black'}; border: 1px solid black")

    def button_click(self, row, col): 
        # Function to be called as the button is clicked
        #print(self.list_forbidden_squares)
        list_possible_moves = self.possible_moves()
        #print(list_possible_moves,len(list_possible_moves))
        if (row, col) in list_possible_moves: # Check if the button is empty
            self.table[row][col].setText(self.current_player)
            self.table[row][col].setStyleSheet(
                f"background-color: {self.get_player_color()}"
            )
            # Disable buttons associated with forbidden squares
            self.list_forbidden_squares.append((row,col))

            # Toggle player
            self.last_square = (row,col)
            self.nbr_square_in_big_square[row//3][col//3] += 1 
            #print(game.current_big_square(self.last_square,self.table))
            #print(game.is_winner(game.current_big_square(self.last_square,self.table),self.current_player))

            if game.is_winner(game.current_big_square(self.last_square,self.table),self.current_player):#verifie si le grand carré a été gagné
                for i in range(3):
                    for j in range(3):
                        if i == row//3 and j == col//3:
                            for k in range(3):
                                for l in range(3):
                                    row2, col2 = 3*i+k,3*j+l
                                    if not ((row2,col2) in self.list_forbidden_squares):# ajoute toutes les cases restantes du carré gagné à la liste des coups interdits 
                                        self.list_forbidden_squares.append((row2,col2))
                self.big_square_table[row//3][col//3]=self.current_player
                #print(self.big_square_table)
                self.create_big_button(row//3,col//3)

                if game.is_winner(self.big_square_table,self.current_player):#vérifie si le jeu est fini 
                    self.disable_all_buttons()
                    print(self.current_player) # ajouter un écran de victoire
                if len(self.list_forbidden_squares)==81: # on ne peut jouer nulle part
                    print("égalité") #ajouter un écran d'égalité

            elif self.nbr_square_in_big_square[row//3][col//3]==9 and not game.is_winner(game.current_big_square(self.last_square,self.table),self.current_player):
                self.color_pat_big_square(row//3,col//3)

            list_possible_moves = self.possible_moves() #on modifie la liste des coups possibles pour le tour suivant
            for i in range(9): # donne aux cases leur couleur de départ (gris ou gris clair)
                for j in range(9):
                    if self.table[i][j].text() == "" :
                        block_color = self.get_block_color(i // 3, j // 3)
                        self.table[i][j].setStyleSheet(
                        f"background-color: {block_color}; border: 1px solid black"
                )
            for (i,j) in list_possible_moves : # colorie les coups possubles en jaune
                self.table[i][j].setStyleSheet(f"background-color: {'yellow'}; border: 1px solid black")
            self.disable_buttons()
            if self.current_player == "O": # modifie le curseur pour indiquer quel joueur doit jouer (un 0 pour le joueur O et un + pour le joueur X)
                self.setCursor(Qt.SizeAllCursor)
            else:
                self.setCursor(Qt.ForbiddenCursor)
            self.current_player = "O" if self.current_player == "X" else "X" #fin du tour, donne la main au joueur suivant


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Board()
    sys.exit(app.exec_())
