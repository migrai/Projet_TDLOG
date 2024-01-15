import random
import game

def IA_random(table, list_possible_moves):
    (row,col) = list_possible_moves[random.randint(0, len(list_possible_moves)-1)]
    return (row,col)

def minimax(board, possible_moves, depth = 0, maximizing_player="O" ):
    # Fonction Minimax pour évaluer tous les mouvements possibles et choisir le meilleur
    if game.is_winner(board, 'X'):
        return -1
    elif game.is_winner(board, 'O'):
        return 1
    elif len(possible_moves)==0:
        return 0

    if maximizing_player=="O":
        max_eval = float('-inf')
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            eval = minimax(board,possible_moves[:index]+possible_moves[index+1:],maximizing_player="X")
            board[i][j] = ' '
        
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'X'
            eval = minimax(board,possible_moves[:index]+possible_moves[index+1:])
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board,possible_moves):
    # Trouve le meilleur mouvement en utilisant l'algorithme Minimax dans le morpion 1D
        best_val = float('-inf')
        best_move = (-1, -1)
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            move_val = minimax(board,possible_moves[:index]+possible_moves[index+1:],maximizing_player="X")
            print("voivi la liste",possible_moves)
            board[i][j] = ' '
            
            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val

        return best_move