import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy


class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the matrix to represent the board
        self.tabuleiro = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ]

        self.resize(900,900)

        # Variable to track the current player (X or O)
        self.current_player = "X"

        # Create the buttons and add them to the matrix
        for i in range(9):
            for j in range(9):
                btn = QPushButton("", self)
                btn.setSizePolicy(
                    QSizePolicy.Expanding, QSizePolicy.Expanding
                )  # Set size policy
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                grid.addWidget(btn, i, j)
                self.tabuleiro[i][j] = btn

                # Increase the font size for larger buttons
                font = btn.font()
                font.setPointSize(20)
                btn.setFont(font)

                # Set background color based on the block position
                block_color = self.get_block_color(i // 3, j // 3)
                btn.setStyleSheet(
                    f"background-color: {block_color}; border: 1px solid black"
                )

        self.setWindowTitle("Meta-Morpion")
        self.show()
    # Ajoutez ces méthodes à votre classe Board

    def disable_buttons(self, list_forbidden_squares):
        # Désactiver les boutons aux coordonnées spécifiées
        for row, col in list_forbidden_squares:
            self.tabuleiro[row][col].setEnabled(False)

    def enable_all_buttons(self):
        # Réactiver tous les boutons
        for row in range(9):
            for col in range(9):
                self.tabuleiro[row][col].setEnabled(True)


    def button_click(self, row, col):
        # Function to be called as the button is clicked
        if not self.tabuleiro[row][col].text():  # Check if the button is empty
            self.tabuleiro[row][col].setText(self.current_player)
            self.tabuleiro[row][col].setStyleSheet(
                f"background-color: {self.get_player_color()}"
            )
            # Désactiver les boutons associés aux cases interdites
            disabled_coordinates = self.get_disabled_coordinates()  # Mettez à jour cette fonction selon vos besoins
            self.disable_buttons(disabled_coordinates)

            # Réactiver tous les boutons pour le prochain tour
            self.enable_all_buttons()

            # Basculer le joueur
            self.current_player = "O" if self.current_player == "X" else "X"

    def get_player_color(self):
        # Return color based on the current player
        return "red" if self.current_player == "X" else "blue"

    def get_block_color(self, row, col):
        # Return alternating colors for the blocks
        return "lightgray" if (row + col) % 2 == 0 else "gray"

    def update_ui(self):
        # Mettez à jour l'interface utilisateur en fonction de l'état du jeu
        # Cela peut inclure la mise à jour des boutons, l'affichage du joueur actuel, etc.
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabuleiro = Board()
    sys.exit(app.exec_())