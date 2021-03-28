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

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return heuristica(position, BLUE), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


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

