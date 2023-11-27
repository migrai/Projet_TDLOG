import board
import build1
import players
import squares
class Game:
    def __init__(self, board_path, player_dict):
        self._board = board.initUI()
        self._current_player_index = 0
        self._number_of_moves = 0
        self._player_list = []
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
    def player_list(self):
        return self._player_list
    @property
    def current_player(self):
        return self._player_list[self._current_player_index]
    @property
    def number_of_moves(self):
        return self._number_of_moves
    
    def possible_squares_for_current_player(self):
        player = self.current_player
        index_possible_squares = []
        if self.number_of_moves() == 0:
            for i in range (len(board.tabuleiro)):
                for j in range (len(board.tabuleiro)):
                    index_possible_squares.append([i,j])
        else:
        return 0
    
    def check_square (self) : #fonction qui vérifie si le dernier coup du joueur gagne une grande case
        # si le coup n'a pas permis de gagner la case elle retourne False, sinon elle retourne le symbole du joueur soit "x" ou "o"
        x = self.last_square.x//3
        y = self.last_square.y//3
        for i in range (3):
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
        
    self.tabuleiro = [[None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None]]

