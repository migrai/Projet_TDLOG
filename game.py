def forbidden_moves_for_current_player(last_square,big_square_table):
    if last_square == None :
        return []
    x, y = last_square[0] % 3, last_square[1] % 3  # coords of the big square which last player points at
    if big_square_table[x][y] != None :
        return []
    forbidden = []
    for i in range(3):
        for j in range(3):
            if i != x or j != y:
                for k in range(3):
                    for l in range(3):
                        forbidden.append((3*i + k, 3*j + l))
    return forbidden

def current_big_square (last_square,table): 
    x, y = last_square[0] // 3, last_square[1] // 3  # coords of the big square which last player points at
    square = []
    for i in range(3):
        for j in range(3):
            if i == x and j == y:
                for k in range(3):
                    row = []
                    for l in range(3):
                        row.append(table[3*i + k][ 3*j + l])
                    square.append(row)
    return square

def is_winner(board, player):
    # Vérifie les lignes, colonnes et diagonales pour déterminer s'il y a un gagnant
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def possible_moves_in_big_square(possible_moves, x_big_square, y_big_square):
    # Returns the list of possible moves in the big square of coordinates (x, y)
    # ATTENTION : resultat sous forme de coordonnées dans [0,2]x[0,2]
    res = []
    for i in range (3):
        for j in range (3):
            if (i+x_big_square*3, j+y_big_square*3) in possible_moves:
                res.append((i,j))
    return res

def current_big_square_state(board_state, x_big_square, y_big_square):
    # returns the list of the state ('X', 'O' or ' ') in the current big square
    res = []
    for i in range(3):
        for j in range(3):
            if i == x_big_square and j == y_big_square:
                for k in range(3):
                    row = []
                    for l in range(3):
                        row.append(board_state[3*i + k][ 3*j + l])
                    res.append(row)
    return res