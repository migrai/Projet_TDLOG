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
    
    def possible_squares_for_current_player(self):  # Returns a list of tuples of the possible moves
        list_possible_squares = []
        if self.number_of_moves() == 0:  # 1st move of the game
            for i in range(len(board.table)):
                for j in range(len(board.table)):
                    list_possible_squares.append((i, j))
        else:  # normal move
            x, y = self.last_square.x % 3, self.last_square.y % 3  # coords of the big square which last player points at
            if self.big_square_table[x][y] is None:  # big square unoccupied
                for i in range(3):
                    for j in range(3):
                        if board.table[3*x+i][3*y+j] is None:  #check that small squares are unoccupied
                            list_possible_squares.append((3*x+i, 3*y+j))

            else:  # occupied big square : every square on the board is possible, as soon as the small square and its big square are unoccupied
                for i_big in range(3):
                    for j_big in range(3):  # indices of big squares
                        if self.big_square_table[i_big][j_big] is None:
                            for i in range(3):
                                for j in range(3):
                                    if board.table[3*i_big+i][3*j_big+j] is None:
                                        list_possible_squares.append((3*i_big+i, 3*j_big+j))
        return list_possible_squares
    
    def forbidden_moves_for_current_player(self):
        list_forbidden_squares = []
        x, y = self.last_square.x % 3, self.last_square.y % 3  # coords of the big square which last player points at
        if self.big_square_table[x][y] is not None:  # big square last player points at is occupied : only forbidden squares are the ones already occupied
            for i_big in range(3):
                for j_big in range(3):
                    if self.big_square_table[i_big][j_big] is not None:  # Big squared occupied : every small square in it is forbidden
                        for i in range(3):
                            for j in range(3):
                                list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
                    else:  #Big square unoccupied : only the small squares that are occupied are forbidden
                        for i in range(3):
                            for j in range(3):
                                if board.table[3*i_big+i][3*j_big+j] is not None:
                                    list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
        else: #big square last player points at is unoccupied 
            #next player can only play in that square so we forbid every other big square
            for i_big in range(3):
                for j_big in range(3):
                    if i_big == x and j_big == y: # big square last player points at
                        # only moves forbidden here are small squares that are already occupied
                        for i in range(3):
                            for j in range(3):
                                if board.table[3*i_big+i][3*j_big+j] is not None:
                                    list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
                    else: #every other big square
                        # every square is forbidden here
                        for i in range(3):
                            for j in range(3):
                                list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
        return list_forbidden_squares
    
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
        else: 
            return False
        
    def check_win(self, big_board_state): #fonction qui dit s'il y a un gagnant DU JEU et si oui quel joueur
        # Vérifiez si un joueur a gagné horizontalement, verticalement ou en diagonale dans les grandes cases
        players = ['X', 'O']
        for player in players:
            for i in range(3):
                # Vérification horizontale
                if (
                    big_board_state[i * 3] == big_board_state[i * 3 + 1] == big_board_state[i * 3 + 2] == player
                    and big_board_state[i * 3] is not None
                ):
                    return player
                # Vérification verticale
                if (
                    big_board_state[i] == big_board_state[i + 3] == big_board_state[i + 6] == player
                    and big_board_state[i] is not None
                ):
                    return player
                # Vérification diagonale
                if (
                    big_board_state[0] == big_board_state[4] == big_board_state[8] == player
                    and big_board_state[0] is not None
                ) or (
                    big_board_state[2] == big_board_state[4] == big_board_state[6] == player
                    and big_board_state[2] is not None
                ):
                    return player #on renvoit le grand gagnant
        return None  # Aucun gagnant pour le moment
        

        


