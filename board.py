import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

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
                          [None, None, None, None, None, None, None, None, None],]

        # Create the buttons and add them to the matrix
        for i in range(9):
            for j in range(9):
                btn = QPushButton('', self)
                btn.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                grid.addWidget(btn, i, j)
                self.tabuleiro[i][j] = btn

        self.setWindowTitle('Meta-Morpion')
        self.show()

    def button_click(self, row, col):
        # Function to be called as the button is clicked
        print(f"Button on line {row} and column {col} was clicked.")

        # Here we can add additional functions, like changing the color

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabuleiro = Board()
    sys.exit(app.exec_())
