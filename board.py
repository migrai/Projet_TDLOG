import sys
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



class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the matrix of buttons to represent the board
        self.table = [[None] * 9 for _ in range(9)]

        # Create the matrix of "X" or "O"
        self.table_state = [[None] * 9 for _ in range(9)]
        self.table_state[0][0] = "X"
        self.table_state[0][1] = "O"

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
                initial_list_forbidden = [(k,l) for k in range(9) for l in range(9)]
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col, initial_list_forbidden))
                grid.addWidget(btn, i, j)
                self.table[i][j] = btn

                # Increase the font size for larger buttons
                self.update_font_size(btn)

                # Set background color based on the block position
                block_color = self.get_big_square_color(i // 3, j // 3)
                btn.setStyleSheet(
                    f"background-color: {block_color}; border: 1px solid black"
                )

                #set background color based on the state of the table
                self.table[i][j].setText(self.table_state[i][j])
                self.table[i][j].setStyleSheet(
                f"background-color: {self.get_player_color(i,j)}; border: 1px solid black"
            )

        self.setWindowTitle("Meta-Morpion")
        self.show()

    def disable_buttons(self, list_forbidden_squares):
        # Désactiver les boutons aux coordonnées spécifiées
        for row, col in list_forbidden_squares:
            self.table[row][col].setEnabled(False)

    def enable_all_buttons(self):
        # Réactiver tous les boutons
        for row in range(9):
            for col in range(9):
                self.table[row][col].setEnabled(True)


    def resizeEvent(self, event):
        # Override the resizeEvent method to handle window resize
        for i in range(9):
            for j in range(9):
                btn = self.table[i][j]
                self.update_font_size(btn)

    def update_font_size(self, button):
        # Update font size based on window width
        font_size = self.width() // 40
        font = button.font()
        font.setPointSize(font_size)
        button.setFont(font)

    def get_player_color(self,row,col):
        #return color based on the state of the square
        if self.table_state[row][col]=="X":
            return "red"
        if self.table_state[row][col]=="O":
            return "blue"
        if self.table_state[row][col]==None:
            return self.get_big_square_color(row//3,col//3)
        
    def get_current_player_color(self):
        # Return color based on the current player
        return "red" if self.current_player == "X" else "blue"

    def get_big_square_color(self, row, col):
        # Return alternating colors for the blocks
        if (row + col) % 2 == 0:
            return "lightgray"
        else:
            return "gray"
        
    def button_click(self, row, col, list_forbidden_squares):
        # Function to be called as the button is clicked
        if not self.table[row][col].text():  # Check if the button is empty
            self.table[row][col].setText(self.current_player)
            self.table[row][col].setStyleSheet(
                f"background-color: {self.get_current_player_color()}"
            )
            self.table_state[row][col] = self.current_player
            # Disable buttons associated with forbidden squares
            self.disable_buttons(list_forbidden_squares)

            # Enable all buttons for the next turn
            self.enable_all_buttons()

            # Toggle player
            last_square = self.table[row][col]

            self.current_player = "O" if self.current_player == "X" else "X"
        print(self.table_state)

    def update_ui(self):
        # Mettez à jour l'interface utilisateur en fonction de l'état du jeu
        # Cela peut inclure la mise à jour des boutons, l'affichage du joueur actuel, etc.
        #l =
        
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Board()
    sys.exit(app.exec_())
