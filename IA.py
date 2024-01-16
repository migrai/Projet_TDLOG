import random
import game

def IA_random(table, list_possible_moves): #marche pour les deux dimensions possibles
    (row,col) = list_possible_moves[random.randint(0, len(list_possible_moves)-1)]
    return (row,col)

def minimax(board, possible_moves, depth = 0, maximizing_player="O"):
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


def find_best_move_1D(board,possible_moves):
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

def find_best_move_big_square(board,possible_moves):
    # Trouve le meilleur mouvement en utilisant l'algorithme Minimax dans le morpion 1D. Mais si l'IA a deux cases alignées
        # et rien dans la 3ème case, elle joue le move pour gagner la case (le problème est que l'IA find_best_move_1D
        # considère que le joueur adverse va jouer un coup pour empêcher la prise de la case, alors qu'en 2D elle joue
        # sans que le joueur adverse puisse jouer avant.

        # étape 1 : vérifier si on peut prendre la grosse case instantanément
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            if game.is_winner(board,'O'):
                print ("can win instantly !")
                return i,j
            board[i][j] = ' ' # remettre le board dans l'état initial.

        # étape 2 : si on ne peut pas gagner instantanément, on cherche le meilleur move.
        return find_best_move_1D(board,possible_moves)

    
def big_square_greedy(possible_moves, last_square, board_state, nbr_square_in_bigsquare):
    # Trouve le meilleur move pour gagner la grosse case actuelle
    # on considère que le big square a des coordonnées dans [0,2] x [0,2] pour utiliser find_best_move_1D
    # puis on repasse en coordonnées "board" (dans [0,8]x[0,8])

    x, y = (last_square[0]%3, last_square[1]%3) #coordonnées du big square actuel
    # print('coords current_big_square :', x, y)

    if nbr_square_in_bigsquare[x][y] == 0: #l'IA a le premier move dans le big square
        # la manière optimale est de jouer dans un coin, dans {0,2}x{0,2}. On choisit un coin au hasard.
        return 2*random.randint(0,1) + 3*x, 2*random.randint(0,1) + 3*y # on repasse en coordonnées "board"
    
    elif nbr_square_in_bigsquare[x][y] < 9: # si le big_square n'est pas plein et non vide
        possible_moves_in_big_square = game.possible_moves_in_big_square(possible_moves,x,y)
        print('possible moves in big square :', possible_moves_in_big_square)
        current_big_square_state = game.current_big_square_state(board_state,x,y)
        print('current big square state :', current_big_square_state)
        row, col = find_best_move_big_square(current_big_square_state, possible_moves_in_big_square)
        return row + 3*x, col + 3*y
    
    else : # le big square est plein
        return IA_random(board_state, possible_moves)
        