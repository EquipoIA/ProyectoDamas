import pygame
from GUI.constants import *
from GUI.game import Game
from IA.IA import *
from minimax.algorithm import *
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Proyecto Damas')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == RED:
            value, new_board = minimaxRed(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        elif game.turn == BLUE:
            #value= negamax(game.get_board(), 4, BLUE,-10000,10000, game)
            #new_board = getMejor_Movimiento()
            value, new_board = minimaxBlue(game.get_board(), 4, BLUE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()