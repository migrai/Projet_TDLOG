import random
import game

### EASY LEVEL (1D, 2D)

def IA_random(list_possible_moves):
    '''Returns a random move among the possible ones'''
    (row,col) = list_possible_moves[random.randint(0, len(list_possible_moves)-1)]
    return (row,col)

### HARD LEVEL 1D
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

### MID LEVEL 2D
        
def win_instantly(board, possible_moves):
    # fonction qui vérifie si l'IA peut prendre la grosse case instantanément
    
    list_greedy_moves = []
    for index, coord in enumerate(possible_moves):
        i,j = coord
        board[i][j] = 'O'
        if game.is_winner(board,'O'): 
            print ("can win square instantly !")
            list_greedy_moves.append((i,j))
        board[i][j] = ' ' # remettre le board dans l'état initial.

    if len(list_greedy_moves) != 0:
        index_res = random.randint(0,len(list_greedy_moves)-1) # prendre un move au hasard parmi ceux qui 
                                                                # prennent la grosse case
        return list_greedy_moves[index_res]
    else :
        return False

def lose_instantly(board, possible_moves):
    # fonction qui vérifie si l'IA peut prendre la grosse case instantanément
    
    list_greedy_moves = []
    for index, coord in enumerate(possible_moves):
        i,j = coord
        board[i][j] = 'X'
        if game.is_winner(board,'X'): 
            print ("can lose square instantly !")
            list_greedy_moves.append((i,j))
        board[i][j] = ' ' # remettre le board dans l'état initial.

    if len(list_greedy_moves) != 0:
        index_res = random.randint(0,len(list_greedy_moves)-1) # prendre un move au hasard parmi ceux qui 
                                                                # prennent la grosse case
        
        return list_greedy_moves[index_res]
    else :
        return False
    
def find_best_move_big_square(board,possible_moves):
    # Trouve le meilleur mouvement en utilisant l'algorithme Minimax dans le morpion 1D. Mais si l'IA a deux cases alignées
        # et rien dans la 3ème case, elle joue le move pour gagner la case (le problème est que l'IA find_best_move_1D
        # considère que le joueur adverse va jouer un coup pour empêcher la prise de la case, alors qu'en 2D elle joue
        # sans que le joueur adverse puisse jouer avant.

        # étape 1 : vérifier si on peut prendre la grosse case instantanément
        if win_instantly(board, possible_moves) != False:
            return win_instantly(board, possible_moves)
        
        # étape 2 : vérifier si le joueur adverse peut prendre la grosse case instantanément
        if lose_instantly(board, possible_moves) != False:
            return lose_instantly(board, possible_moves)

        # étape 2 : si on ne peut pas gagner instantanément, on cherche le meilleur move.
        else:
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
        print('full big_square')
        # on parcourt l'ensemble des autres big_square pour voir si l'un d'entre eux est gagnable immédiatement
        list_greedy_moves = []
        for i_big in range(3):
            for j_big in range(3):
                if nbr_square_in_bigsquare[i_big][j_big] < 9:
                    possible_moves_in_big_square = game.possible_moves_in_big_square(possible_moves,i_big,j_big)
                    board_big_square = game.current_big_square_state(board_state,i_big,j_big)
                    if win_instantly(board_big_square, possible_moves_in_big_square) != False:
                        move_0_2 = win_instantly(board_big_square, possible_moves_in_big_square) # coords in [0,2]x[0,2]
                        move_0_8 = (move_0_2[0]+3*i_big, move_0_2[1]+3*j_big)
                        list_greedy_moves.append(move_0_8)
        if len(list_greedy_moves) > 0: # un move gagnant une grosse case existe
            return list_greedy_moves[random.randint(0,len(list_greedy_moves)-1)] # on prend un move gagnant au hasard
        return IA_random(board_state, possible_moves)
        
### HARD MODE 2D
    
def minimax_2D(last_square,alpha,beta,board, board_big_square, possible_moves, forbidden_moves, depth ,score = 0 , maximizing_player="O" ):
    # Fonction Minimax pour évaluer tous les mouvements possibles et choisir le meilleur
    if depth <= 0 :
        return score
    elif game.is_winner(game.current_big_square(last_square,board),"X"):#verifie si le grand carré a été gagné
        #print("entré", depth)
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves):# ajoute toutes les cases restantes du carré gagné à la liste des coups interdits 
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="X"
        score -= 10
        
        if game.is_winner(board_big_square,"X"):#vérifie si le jeu est fini 
            return -100
    elif game.is_winner(game.current_big_square(last_square,board),"O"):#verifie si le grand carré a été gagné
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves):# ajoute toutes les cases restantes du carré gagné à la liste des coups interdits 
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="O"
        score += 10
        
        if game.is_winner(board_big_square,"O"):#vérifie si le jeu est fini 
            return 100
    elif len(forbidden_moves) == 81 :
        return 0
    else : 
        score += random.random()
    if maximizing_player=="O":
        max_eval = float('-inf')
        #print(possible_moves)
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            sauvegarde = possible_moves[:]
            forbidden_moves.append(coord)
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            """
            if depth !=1 :
                print("profondeur : ", depth , "score : ", score, "joueur : ", maximizing_player)
            """
            eval = minimax_2D(coord,alpha,beta,board,board_big_square,possible_moves,forbidden_moves,score=score,depth=depth-1,maximizing_player="X")
            board[i][j] = ' '
            forbidden_moves.pop()
            possible_moves = sauvegarde[:]
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Élagage Alpha-Beta
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        #print(possible_moves)
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'X'
            sauvegarde = possible_moves[:]
            forbidden_moves.append(coord)
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            """depth !=1 :
                print("profondeur : ", depth , "score : ", score, "joueur : ", maximizing_player)
            """
            eval = minimax_2D(coord,alpha,beta,board,board_big_square,possible_moves,forbidden_moves,score=score,depth=depth-1)
            board[i][j] = ' '
            forbidden_moves.pop()
            possible_moves = sauvegarde[:]
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Élagage Alpha-Beta
            min_eval = min(min_eval, eval)
        return min_eval

"""
def find_best_move_2D(last_square,board,board_big_square,possible_moves,forbidden_moves,depth=5):
    # Trouve le meilleur mouvement en utilisant l'algorithme Minimax dans le morpion 1D
        best_val = float('-inf')
        best_move = (-1, -1)
        alpha = float('-inf')
        beta = float('inf')
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            sauvegarde = possible_moves[:]
            forbidden_moves.append(coord)
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            move_val = minimax_2D(last_square,alpha,beta,board,board_big_square,possible_moves,forbidden_moves,depth=4,maximizing_player="X")
            #print("coup : ",(i,j),move_val)
            board[i][j] = ' '
            forbidden_moves.pop()
            possible_moves = sauvegarde[:] 
            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val
                #print(best_move,best_val)
        print(possible_moves)
        return best_move
        """
def alpha_beta(last_square,alpha,beta,board, board_big_square, possible_moves, forbidden_moves, depth ,score = 0 , maximizing_player="O" ):
    # Fonction Minimax pour évaluer tous les mouvements possibles et choisir le meilleur
    if depth <= 0 :
        return score
    elif game.is_winner(game.current_big_square(last_square,board),"X"):#verifie si le grand carré a été gagné
        #print("entré", depth)
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves):# ajoute toutes les cases restantes du carré gagné à la liste des coups interdits 
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="X"
        score -= 10
        
        if game.is_winner(board_big_square,"X"):#vérifie si le jeu est fini 
            return -100
    elif game.is_winner(game.current_big_square(last_square,board),"O"):#verifie si le grand carré a été gagné
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves):# ajoute toutes les cases restantes du carré gagné à la liste des coups interdits 
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="O"
        score += 10
        
        if game.is_winner(board_big_square,"O"):#vérifie si le jeu est fini 
            return 100
    elif len(forbidden_moves)== 81 :
        return 0
    else : 
        score += random.random()
    if maximizing_player=="O":
        max_eval = float('-inf')
        #print(possible_moves)
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            sauvegarde_p = possible_moves[:]
            sauvegarde_f = forbidden_moves
            forbidden_moves.append(coord)
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            """
            if depth !=1 :
                print("profondeur : ", depth , "score : ", score, "joueur : ", maximizing_player)
            """
            eval = alpha_beta(coord,alpha,beta,board,board_big_square,possible_moves,forbidden_moves,score=score,depth=depth-1,maximizing_player="X")
            board[i][j] = ' ' 
            possible_moves = sauvegarde_p[:]
            forbidden_moves = sauvegarde_f[:]
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Élagage Alpha-Beta
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        #print(possible_moves)
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'X'
            sauvegarde_p = possible_moves[:]
            sauvegarde_f = forbidden_moves
            forbidden_moves.append(coord)
            
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            """depth !=1 :
                print("profondeur : ", depth , "score : ", score, "joueur : ", maximizing_player)
            """
            eval = alpha_beta(coord,alpha,beta,board,board_big_square,possible_moves,forbidden_moves,score=score,depth=depth-1)
            board[i][j] = ' '
            forbidden_moves = sauvegarde_f[:]
            possible_moves = sauvegarde_p[:]
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Élagage Alpha-Beta
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move_2D(last_square,board,board_big_square,possible_moves,forbidden_moves,depth=5):
    # Trouve le meilleur mouvement en utilisant l'algorithme Minimax dans le morpion 1D
        best_val = float('-inf')
        best_move = possible_moves[0]
        alpha = float('-inf')
        beta = float('inf')
        print(possible_moves)
        copy_board_big_square = board_big_square.copy()
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            #print(board,index)
            print(forbidden_moves,"index",index)
            sauvegarde_p = possible_moves[:]
            sauvegarde_f = forbidden_moves[:]
            forbidden_moves.append(coord)
            possible_moves = game.possible_moves(forbidden_moves,board_big_square,coord)
            move_val = alpha_beta(last_square,alpha,beta,board,copy_board_big_square,possible_moves,forbidden_moves,depth,maximizing_player="X")
            #print("coup : ",(i,j),move_val)
            board[i][j] = ' '
            forbidden_moves = sauvegarde_f[:]
            possible_moves = sauvegarde_p[:] 
            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val
                #print(best_move,best_val)
            #print(board)
            print(forbidden_moves)
        #print(possible_moves)
        print(forbidden_moves,"sortie_IA")
        return best_move