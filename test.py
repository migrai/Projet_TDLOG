import game

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
last_square_test = [4,4]
number_of_moves_test = 10
print(game.possible_squares_for_current_player(table_test,big_square_table_test,last_square_test,number_of_moves_test))
print(game.forbidden_moves_for_current_player(table_test,big_square_table_test,last_square_test))

initial_list_forbidden = [(k,l) for k in range(9) for l in range(9)]
print(initial_list_forbidden)