import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.blue_left = 12
        self.red_kings = self.blue_kings = 0
        self.create_board() 
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == BLUE:
                self.blue_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2): #revisamos que la posición sea donde va una ficha 
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLUE))#si la fila es menor a 3 añadimos una ficha roja 
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED)) #si la fila es mayor a 4 añadimos una ficha azul 
                    else:
                        self.board[row].append(0) #añadimos espacios vacios en la parte media del tablero 
                else:
                    self.board[row].append(0) #añadimos espacios vacíos en todas las posiciones entre las fichas
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.blue_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return BLUE
        elif self.blue_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
        #print(moves)
        return moves

#Checa los moviminetos posibles empezando hacia la izquierda
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {} #diccionario con los movimientos y las piezas que se come en cada uno
        last = [] #variable que indica si la posicion de antes comimos una pieza
        for r in range(start, stop, step):#for que checa dos filas hacia arriba o hacia abajo dependiendo el caso
            if left < 0: #checa si la posicion que queremos checar es valida
                break
            
            current = self.board[r][left]
            if current == 0:#checa si al posicion a la que nos queremos mover esta vacia
                if skipped and not last: #si ya habiamos comido alguien, no se puede mover a otro vacio despues
                    break
                elif skipped:#agrega el movimiento mas las que ya habia comido
                    moves[(r, left)] = last + skipped
                else:#agrega el movimiento (si last es vacia, es que no come a nadie)
                    moves[(r, left)] = last
                
                if last: #si ya habiamos comido, hace una llamada recursiva par ver si puede volver a comer
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color: #si la ficha es del mismo color, no puede avanzar
                break
            else: #si es de color distinto, la agrega a las fichas que puede comer
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
