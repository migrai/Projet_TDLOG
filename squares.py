class Square:
    def __init__(self):
        self.state = "unoccupied"  # L'état initial est inoccupé


class SmallSquare(Square):
    def __init__(self):
        self.state = "unoccupied"  # L'état initial est inoccupé

    def occupy(self, color):
        self.state = "occupied_" + color  # "occupied_blue" ou "occupied_red"


class BigSquare(Square):
    def __init__(self):
        self.state = "unoccupied"  # L'état initial est inoccupé

    def occupy(self, color):
        self.state = "occupied_" + color  # "occupied_blue" ou "occupied_red"
    
    def next_move(self, color):
        self.state = 
