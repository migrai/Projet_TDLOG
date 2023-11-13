import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the matrix to represent the board
        self.tabuleiro = [[None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None]]

        # Variable to track the current player (X or O)
        self.current_player = 'X'

        # Create the buttons and add them to the matrix
        for i in range(9):
            for j in range(9):
                btn = QPushButton('', self)
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                btn.setStyleSheet("background-color: white; border: 1px solid black")
                grid.addWidget(btn, i, j)
                self.tabuleiro[i][j] = btn

                # Increase the font size for larger buttons
                font = btn.font()
                font.setPointSize(20)
                btn.setFont(font)

                # Set the minimum and maximum size to ensure the button is square
                min_size = min(btn.sizeHint().width(), btn.sizeHint().height())
                btn.setMinimumSize(min_size, min_size)
                btn.setMaximumSize(min_size, min_size)

        self.setWindowTitle('Meta-Morpion')
        self.show()

    def button_click(self, row, col):
        # Function to be called as the button is clicked
        if not self.tabuleiro[row][col].text():  # Check if the button is empty
            self.tabuleiro[row][col].setText(self.current_player)
            self.tabuleiro[row][col].setStyleSheet(f'background-color: {self.get_player_color()}')

            # Toggle player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_color(self):
        # Return color based on the current player
        return 'red' if self.current_player == 'X' else 'blue'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabuleiro = Board()
    sys.exit(app.exec_())