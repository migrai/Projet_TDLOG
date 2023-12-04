import board
import players
import squares
class Game:
    def __init__(self, player_dict):
        self._board = board.Board()
        self._big_square_table = [[None for i in range(3)] for j in range(3)]  # 3x3 of big squares
        self._current_player_index = 0
        self._number_of_moves = 0
        self._player_list = []
        self._last_square_index = [-1,-1]
        num_players = len(player_dict)
        for player_color, player_name in player_dict.items():
            if player_name is None:
                player = players.RandomPlayer(
                    color=player_color
                )
            else:
                player = players.HumanPlayer(
                    name=player_name,
                    color=player_color,
                )
            self._player_list.append(player)

    @property
    def board(self):
        return self._board
    @property
    def big_square_table(self):
        return self._big_square_table
    @property
    def last_square_index(self):
        return self._last_square_index
    @property
    def player_list(self):
        return self._player_list
    @property
    def current_player(self):
        return self._player_list[self._current_player_index]
    @property
    def number_of_moves(self): 
        return self._number_of_moves
    
    def possible_squares_for_current_player(self):
        index_possible_squares = []
        if self.number_of_moves() == 0:  # 1st move of the game
            for i in range(len(board.table)):
                for j in range(len(board.table)):
                    index_possible_squares.append((i, j))
        else:  # normal move
            x, y = self.last_square.x % 3, self.last_square.y % 3  # coords of the big square which last player points at
            if self.big_square_table[x][y] is None:  # big square unoccupied
                for i in range(3):
                    for j in range(3):
                        if board.table[3*x+i][3*y+j] is None:  #check that small squares are unoccupied
                            index_possible_squares.append((3*x+i, 3*y+j))
            else:  # occupied big square : every square on the board is possible, as soon as the small square and its big square are unoccupied
                for i_big in range(3):
                    for j_big in range(3):  # indices of big squares
                        if self.big_square_table[i_big][j_big] is None:
                            for i in range(3):
                                for j in range(3):
                                    if board.table[3*i_big+i][3*j_big+j] is None:
                                        index_possible_squares.append((3*i_big+i, 3*j_big+j))
        return index_possible_squares
    
    
    
    def check_ifsquarewon(self) :  #fonction qui vérifie si le dernier coup du joueur gagne une grande case
        # si le coup n'a pas permis de gagner la case elle retourne False, sinon elle retourne le symbole du joueur soit "x" ou "o"
        #doit modifier le big_square_table en ajoutant "x" ou "o" dans ce cas
        x = self.last_square.x//3
        y = self.last_square.y//3
        for i in range(3):
            if self.table[3*x+i][3*y]==self.table[3*x+i][3*y+1]==self.table[3*x+i][3*y+2] : 
                return self.table[self.last_square.x][self.last_square.y]
            if self.table[3*x][3*y+i]==self.table[3*x+1][3*y+i]==self.table[3*x+2][3*y+i] : 
                return self.table[self.last_square.x][self.last_square.y]
        if self.table[3*x][3*y]==self.table[3*x+1][3*y+1]==self.table[3*x+2][3*y+2] : 
            return self.table[self.last_square.x][self.last_square.y]
        if self.table[3*x+2][3*y]==self.table[3*x+1][3*y+1]==self.table[3*x][3*y+2] : 
            return self.table[self.last_square.x][self.last_square.y]
        else : 
            return False
        
#only used for testing the function (class game not working properly) 
def possible_squares_for_current_player(table,big_square_table,last_square,number_of_moves):
        index_possible_squares = []
        if number_of_moves == 0:  # 1st move of the game
            for i in range(len(table)):
                for j in range(len(table)):
                    index_possible_squares.append((i, j))
        else:  # normal move
            x, y = last_square[0] % 3, last_square[1] % 3  # coords of the big square which last player points at
            if big_square_table[x][y] is None:  # big square unoccupied
                for i in range(3):
                    for j in range(3):
                        if table[3*x+i][3*y+j] is None:  #check that small squares are unoccupied
                            index_possible_squares.append((3*x+i, 3*y+j))
            else:  # occupied big square : every square on the board is possible, as soon as the small square and its big square are unoccupied
                for i_big in range(3):
                    for j_big in range(3):  # indices of big squares
                        if big_square_table[i_big][j_big] is None:
                            for i in range(3):
                                for j in range(3):
                                    if table[3*i_big+i][3*j_big+j] is None:
                                        index_possible_squares.append((3*i_big+i, 3*j_big+j))
        return index_possible_squares  

table_test = [
            [0, None, None, 1, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, 0, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, 0,0, None, None, None, None],
            [None, None, None, 1, 1, 1, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [0, None, None, None, None, None, 1, None, None],
            [None, None, None, None, None, None, None, None, None],
        ]

big_square_table_test = [[None, None, None],[None, 1, None],[None,None,None]]
last_square_test = [5,5]
number_of_moves_test = 10
print(possible_squares_for_current_player(table_test,big_square_table_test,last_square_test,number_of_moves_test))