import board
import build1
import players
import squares
class Game:
    def __init__(self, board_path, player_dict):
        self._board = board.initUI()
        self._current_player_index = 0
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
    @property
    def current_player(self):
        return self._player_list[self._current_player_index]
    def possible_moves_for_current_player(self):
        player = self.current_player