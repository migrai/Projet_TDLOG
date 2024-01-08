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
                        row.append(table[3*i + k][ 3*j + l].text())
                    square.append(row)
    return square

def is_winner(board, player):
    # Vérifie les lignes, colonnes et diagonales pour déterminer s'il y a un gagnant
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

