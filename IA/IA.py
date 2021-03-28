import pygame

from copy import deepcopy
from GUI.game import Game
from GUI.piece import Piece

BLUE = (60, 39, 173)
RED = (255,0,0)

global mejor_movimiento

def getMejor_Movimiento():
    return mejor_movimiento

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
def negamax(tablero,nivel,jugador,alpha,beta,game):
        mejor_movimiento = None
        if nivel == 0 or tablero.winner()!=None:
            return heuristica(tablero,jugador)
        for movimiento in movimientos_posibles(tablero,jugador,game):
            if jugador == BLUE:
                jugador = RED
            else:
                jugador = BLUE
            valor_temp = -negamax(movimiento,nivel-1,jugador,-beta,-alpha,game)
            if valor_temp >= alpha:
                if nivel==0:
                    mejor_movimiento = movimiento
                alpha = valor_temp
            if alpha >= beta:
                break
        return alpha
def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
def movimientos_posibles(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves