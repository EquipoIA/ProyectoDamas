from copy import deepcopy
import pygame

RED = (255,0,0)
BLUE = (60, 39, 173)

def heuristica(tablero, jugador): #Darle valor a cada tablero según su estado 
        valor = 0
        for i in range(8):
            for j in range(8):
                pos = tablero.get_piece(i,j)
                if pos != 0:
                    if pos.color == jugador:#Si la ficha es del color del jugador en turno suma  
                        if pos.king:
                            valor += 2 #rey suma 2
                        else:
                            valor += 1 #ficha normal suma 1
                    else:
                        if pos.king:
                            valor -= 2 #rey enemigo resta 2 
                        else:
                            valor -= 1 #ficha enemiga resta 1 
                    if pos.color == RED:
                        if j<=4:
                            valor += 0.5 #verificamos si la ficha está en la mitad del rival 
                    else:
                        if j>=3:
                            valor += 0.5 #verificamos si la ficha esta en la mitad del rival 
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

#Algoritmo minimax con alpha beta
def minimaxBlue(position, depth, max_player,alpha,beta):
    if depth == 0 or position.winner() != None: #si ya bajamos al ultimo nivel permitido o ya no tiene hijos
        return heuristica(position, BLUE), position
    
    if max_player:#si estamos buscando maximizar el valor
        best_move = None
        value = -10000
        for move in get_all_moves(position, BLUE): #recorre los hijos del nodo en el que estamos
            evaluation = minimaxBlue(move, depth-1, False,alpha, beta)[0]
            if evaluation > value:
                value = evaluation
            if value > alpha:#si el valor del hijo es mayor a alpha, se hace el cambio
                alpha = evaluation
                best_move = move
            if alpha >= beta: #parte que hace el "pruning" de las ramas
                return value, best_move  
        return value,best_move
    else: #si estamos buscanod minimizar el valor
        best_move = None
        value = 10000
        for move in get_all_moves(position, RED):#recorre los hijos del nodo en el que estamos
            evaluation = minimaxBlue(move, depth-1, True,alpha,beta)[0]
            if evaluation < value:
                value = evaluation
            if value < beta: #si el valor es menor a beta, se hace el cambio
                beta = evaluation
                best_move = move
            if alpha >= beta:#parte que hace el "pruning" de las ramas
                return value,best_move   
        return value, best_move


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board,skip)
            moves.append(new_board)
    return moves

