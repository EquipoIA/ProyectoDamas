from copy import deepcopy
import pygame

RED = (255,0,0)
BLUE = (60, 39, 173)

def heuristica(tablero, jugador):
        valor = 0
        for i in range(8):
            for j in range(8):
                pos = tablero.get_piece(i,j)
                if pos != 0:
                    if pos.color == jugador:
                        if pos.king:
                            valor += 2
                        else:
                            valor += 1
                    else:
                        if pos.king:
                            valor -= 2
                        else:
                            valor -= 1
        return valor

def minimaxRed(position, depth, max_player,alpha,beta, game):
    if depth == 0 or position.winner() != None:
        return heuristica(position, RED), position
    
    if max_player:
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimaxBlue(move, depth-1, False,alpha, beta, game)[0]
            if evaluation > alpha:
                alpha = evaluation
                best_move = move
            if alpha >= beta:
                return alpha, best_move  
        return alpha,best_move
    else:
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimaxBlue(move, depth-1, True,alpha,beta, game)[0]
            if evaluation < beta:
                beta = evaluation
                best_move = move
            if alpha >= beta:
                return beta,best_move   
        return beta, best_move

def minimaxBlue(position, depth, max_player,alpha,beta, game):
    if depth == 0 or position.winner() != None:
        return heuristica(position, BLUE), position
    
    if max_player:
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimaxBlue(move, depth-1, False,alpha, beta, game)[0]
            if evaluation > alpha:
                alpha = evaluation
                best_move = move
            if alpha >= beta:
                return alpha, best_move  
        return alpha,best_move
    else:
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimaxBlue(move, depth-1, True,alpha,beta, game)[0]
            if evaluation < beta:
                beta = evaluation
                best_move = move
            if alpha >= beta:
                return beta,best_move   
        return beta, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def simula_mov(piece,move,board,game,skip):
    temp_tablero = deepcopy(board)
    temp_tablero.move(piece, move[0], move[1])
    if skip:
        temp_tablero.remove(skip)
    return temp_tablero

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
        #draw_moves(game, board, piece)
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)

