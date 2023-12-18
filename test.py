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

#only used for testing the function (class game not working properly) 
def possible_squares_for_current_player(table,big_square_table,last_square,number_of_moves):
        list_possible_squares = []
        if number_of_moves == 0:  # 1st move of the game
            for i in range(len(table)):
                for j in range(len(table)):
                    list_possible_squares.append((i, j))
        else:  # normal move
            x, y = last_square[0] % 3, last_square[1] % 3  # coords of the big square which last player points at
            if big_square_table[x][y] is None:  # big square unoccupied
                for i in range(3):
                    for j in range(3):
                        if table[3*x+i][3*y+j] is None:  #check that small squares are unoccupied
                            list_possible_squares.append((3*x+i, 3*y+j))
            else:  # occupied big square : every square on the board is possible, as soon as the small square and its big square are unoccupied
                for i_big in range(3):
                    for j_big in range(3):  # indices of big squares
                        if big_square_table[i_big][j_big] is None:
                            for i in range(3):
                                for j in range(3):
                                    if table[3*i_big+i][3*j_big+j] is None:
                                        list_possible_squares.append((3*i_big+i, 3*j_big+j))
        return list_possible_squares 

def forbidden_moves_for_current_player(table,big_square_table,last_square):
    list_forbidden_squares = []
    x, y = last_square[0] % 3, last_square[1] % 3  # coords of the big square which last player points at
    if big_square_table[x][y] is not None:  # big square last player points at is occupied : only forbidden squares are the ones already occupied
        for i_big in range(3):
            for j_big in range(3):
                if big_square_table[i_big][j_big] is not None:  # Big squared occupied : every small square in it is forbidden
                    for i in range(3):
                        for j in range(3):
                            list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
                else:  #Big square unoccupied : only the small squares that are occupied are forbidden
                    for i in range(3):
                        for j in range(3):
                            if table[3*i_big+i][3*j_big+j] is not None:
                                list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
    else: #big square last player points at is unoccupied 
        #next player can only play in that square so we forbid every other big square
        for i_big in range(3):
            for j_big in range(3):
                if i_big == x and j_big == y: # big square last player points at
                    # only moves forbidden here are small squares that are already occupied
                    for i in range(3):
                        for j in range(3):
                            if table[3*i_big+i][3*j_big+j] is not None:
                                list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
                else: #every other big square
                    # every square is forbidden here
                    for i in range(3):
                        for j in range(3):
                            list_forbidden_squares.append((3*i_big+i, 3*j_big+j))
    return list_forbidden_squares

big_square_table_test = [[None, None, None],[None, 1, None],[None,None,None]]
last_square_test = [4,4]
number_of_moves_test = 10
game.possible_squares_for_current_player(table_test,big_square_table_test,last_square_test,number_of_moves_test)
game.forbidden_moves_for_current_player(table_test,big_square_table_test,last_square_test)
