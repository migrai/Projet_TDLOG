edge_size = 3 # number of squares in an edge of a classic tic-tac-toe board
edge_size_smls = 9 # number of small squares in an edge of the board
edge_size_bigs = 3 # number of big squares in an edge of the board
edge_size_in_bigs = edge_size_smls//edge_size_bigs # number of small squares in an edge of a big square

def forbidden_moves_for_current_player(last_square, big_square_table):
    #Returns the list of the forbidden moves in the big_square_table, depending of the last move played
    if last_square == None:
        return []
    x, y = last_square[0] % edge_size_bigs, last_square[1] % edge_size_bigs  # coords of the big square which last player points at
    if big_square_table[x][y] != None:
        return []
    forbidden = []
    for row_big_s in range(edge_size_bigs):
        for col_big_s in range(edge_size_bigs):
            if row_big_s != x or col_big_s != y:
                for row_in_bigs in range(edge_size_in_bigs):
                    for col_in_bigs in range(edge_size_in_bigs):
                        forbidden.append((edge_size_in_bigs*row_big_s + row_in_bigs, 
                                          edge_size_in_bigs*col_big_s + col_in_bigs))
    return forbidden

def current_big_square(last_square,table): 
    #Returns the state of the squares in the current big square
    x, y = last_square[0] // edge_size_bigs, last_square[1] // edge_size_bigs  # coords of the big square which last player points at
    square = []
    for row_in_bigs in range(edge_size_in_bigs):
        row = []
        for col_in_bigs in range(edge_size_in_bigs):
            row.append(table[edge_size_in_bigs*x + row_in_bigs][edge_size_in_bigs*y + col_in_bigs])
        square.append(row)
    return square

def is_winner(board, player):
    '''Returns the bool : 1 if there is a winner, 0 otherwise'''
    board_edge_size = len(board)
    print(len(board))
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[row][col] == player for row in range(board_edge_size)) for col in range(board_edge_size)) or \
           all(board[row][row] == player for row in range(board_edge_size)) or \
           all(board[row][2 - row] == player for row in range(board_edge_size))

def possible_moves_in_big_square(possible_moves, x_big_square, y_big_square):
    '''Returns the list of possible moves in the big square of coordinates (x_big_square, y_big_square).
    CAUTION : result under the form of cooridnates in [0,edge_size_in_bigs]x[0,edge_size_in_bigs]'''
    res = []
    for row_in_bigs in range(edge_size_in_bigs):
        for col_in_bigs in range(edge_size_in_bigs):
            if (row_in_bigs+x_big_square*edge_size_in_bigs, col_in_bigs+y_big_square*edge_size_in_bigs) in possible_moves:
                res.append((row_in_bigs,col_in_bigs))
    return res

def current_big_square_state(board_state, x_big_square, y_big_square):
    '''Returns the list of the state ('X', 'O' or ' ') in the current big square'''
    res = []
    for row_in_bigs in range(edge_size_in_bigs):
        for col_in_bigs in range(edge_size_in_bigs):
            if row_in_bigs == x_big_square and col_in_bigs == y_big_square:
                for k in range(edge_size_in_bigs):
                    row = []
                    for l in range(edge_size_in_bigs):
                        row.append(board_state[edge_size_in_bigs*row_in_bigs + k][ edge_size_in_bigs*col_in_bigs + l])
                    res.append(row)
    return res