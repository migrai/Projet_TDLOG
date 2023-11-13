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
    
    self.tabuleiro = [[None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None, None]]
