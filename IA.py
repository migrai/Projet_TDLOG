import random
import game

### EASY LEVEL (1D, 2D)

def IA_random(list_possible_moves):
    '''Returns a random move among the possible ones'''
    (row,col) = list_possible_moves[random.randint(0, len(list_possible_moves)-1)]
    return (row,col)

### HARD LEVEL 1D
def minimax(board, possible_moves, maximizing_player="O"):
    '''Evaluates all possible moves, returns the score of the best one. 
    To do so, it computes recursively all possibilities for next moves'''
    # Stop condition : Score = 1 if the move is winning, -1 if losing, 0 if tied. 
    if game.is_winner(board, 'X'):
        return -1
    elif game.is_winner(board, 'O'):
        return 1
    elif len(possible_moves)==0:
        return 0
    
    # Recursion
    # POV of the AI. So it will try to minimize the score for player 'O'
    if maximizing_player=="O":
        max_eval = float('-inf')
        for index, coord in enumerate(possible_moves):
            i,j = coord
            board[i][j] = 'O'
            eval = minimax(board,possible_moves[:index]+possible_moves[index+1:],maximizing_player="X")
            board[i][j] = ' '
        
            max_eval = max(max_eval, eval)
        return max_eval
    # The AI will try to maximize its own score
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
    '''Returns the best move, using minimax algorithm'''
    best_val = float('-inf')
    best_move = (-1, -1)
    for index, coord in enumerate(possible_moves):
        i,j = coord
        board[i][j] = 'O'
        move_val = minimax(board,possible_moves[:index]+possible_moves[index+1:],maximizing_player="X")
        board[i][j] = ' '
        
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

### MID LEVEL 2D
        
def win_instantly(board, possible_moves, player):
    '''Returns the coordinates of a random move that is winning in one move 
    for the player if it exists, False otherwise'''
    list_greedy_moves = []
    for index, coord in enumerate(possible_moves):
        i,j = coord
        board[i][j] = player
        if game.is_winner(board,player): 
            list_greedy_moves.append((i,j))
        board[i][j] = ' ' # Put the board back in its original state

    if len(list_greedy_moves) != 0:
        index_res = random.randint(0,len(list_greedy_moves)-1) # Pick a random move among the winning ones
        return list_greedy_moves[index_res]
    else :
        return False
    
def find_best_move_big_square(board,possible_moves):
    '''Returns the best move to win the big square using minimax algorithm in morpion1D.'''

    # It's required to check the one-movers, because the minimax algorithm
        # Step 1 : can I win in one move ?
    if win_instantly(board, possible_moves, 'X') != False:
        return win_instantly(board, possible_moves)
    
    # Step 2 : can I lose in one move ?
    if win_instantly(board, possible_moves, 'O') != False:
        return win_instantly(board, possible_moves, 'O')

    # Step 3 : else, I find the best move in the big square I can play in.
    else:
        return find_best_move_1D(board,possible_moves)

    
def big_square_greedy(possible_moves, last_square, board_state, nbr_square_in_bigsquare):
    '''Returns the best move if only a big square is available, a random one otherwise.'''

    x, y = (last_square[0] % game.edge_size_in_bigs, last_square[1] % game.edge_size_in_bigs) # coords of the current big square

    if nbr_square_in_bigsquare[x][y] == 0: #AI has the first move in the big square (empty big square)
        # optimal way to play : in the corner {0,edge_size_in_bigs-1}x{0,edge_size_in_bigs-1}. We choose a random corner.
        return ((game.edge_size_in_bigs-1)*random.randint(0,1) + game.edge_size_in_bigs*x,
                (game.edge_size_in_bigs-1)*random.randint(0,1) + game.edge_size_in_bigs*y) #get back to "board" coords
    
    elif nbr_square_in_bigsquare[x][y] < game.edge_size_in_bigs**2: # big square not full
        possible_moves_in_big_square = game.possible_moves_in_big_square(possible_moves,x,y)
        current_big_square_state = game.current_big_square_state(board_state,x,y)
        row, col = find_best_move_big_square(current_big_square_state, possible_moves_in_big_square)
        return row + game.edge_size_in_bigs*x, col + game.edge_size_in_bigs*y
    
    else : # Full big square
        # We check all the big squares to see if one of them is winnable in one move
        list_greedy_moves = []
        for i_big in range(game.edge_size_bigs):
            for j_big in range(game.edge_size_bigs):
                if nbr_square_in_bigsquare[i_big][j_big] < game.edge_size_in_bigs**2:
                    possible_moves_in_big_square = game.possible_moves_in_big_square(possible_moves,i_big,j_big)
                    board_big_square = game.current_big_square_state(board_state,i_big,j_big)
                    if win_instantly(board_big_square, possible_moves_in_big_square) != False:
                        move_0_2 = win_instantly(board_big_square, possible_moves_in_big_square) # coords in [0,edge_size_in_bigs]x[0,edge_size_in_bigs]
                        move_0_8 = (move_0_2[0]+game.edge_size_in_bigs*i_big, move_0_2[1]+game.edge_size_in_bigs*j_big)
                        list_greedy_moves.append(move_0_8)
        if len(list_greedy_moves) > 0: # There is indeed a winning move
            return list_greedy_moves[random.randint(0,len(list_greedy_moves)-1)] # on prend un move gagnant au hasard
        return IA_random(board_state, possible_moves)
        
### HARD MODE 2D : Work in progress
    
def minimax_2D(last_square,alpha,beta,board, board_big_square, possible_moves, forbidden_moves, depth ,score = 0 , maximizing_player="O" ):
    '''Minimax function to find the best move'''
    if depth <= 0 :
        return score
    elif game.is_winner(game.current_big_square(last_square,board),"X"):#checks if the big_square is won
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves): # adds all empty squares to the list of forbidden moves
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="X"
        score -= 10
        
        if game.is_winner(board_big_square,"X"): # checks if the game is over
            return -100
    elif game.is_winner(game.current_big_square(last_square,board),"O"): # checks if the big square is won
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves): # adds all empty squares to the list of forbidden moves
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="O"
        score += 10
        
        if game.is_winner(board_big_square,"O"): # checks is the game is over
            return 100
    elif len(forbidden_moves) == 81 :
        return 0
    else : 
        score += random.random()
    if maximizing_player=="O":
        max_eval = float('-inf')
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
                break  # Alpha-Beta
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
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
    '''Minimax to find the best move'''
    if depth <= 0 :
        return score
    elif game.is_winner(game.current_big_square(last_square,board),"X"): # checks if the big square is won
        #print("entré", depth)
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves): # adds all remaining empty squares to the list of forbidden moves
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="X"
        score -= 10
        
        if game.is_winner(board_big_square,"X"): # checks if the game is over
            return -100
    elif game.is_winner(game.current_big_square(last_square,board),"O"): # checks if the big square is won
        for i in range(3):
            for j in range(3):
                if i == last_square[0]//3 and j == last_square[1]//3:
                    for k in range(3):
                        for l in range(3):
                            row2, col2 = 3*i+k,3*j+l
                            if not ((row2,col2) in forbidden_moves): # adds all remaining empty squares to the list of forbidden moves
                                forbidden_moves.append((row2,col2))
        board_big_square[last_square[0]//3][last_square[1]//3]="O"
        score += 10
        
        if game.is_winner(board_big_square,"O"): # checks if the game is over
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
                break # alpha beta
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
                break  # alpha beta
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move_2D(last_square,board,board_big_square,possible_moves,forbidden_moves,depth=5):
    ''' Finds the best move using Minimax algorithm'''
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