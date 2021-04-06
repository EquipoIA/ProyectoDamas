import pygame
import pyautogui

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

    eleccion = pyautogui.confirm(text="Escoga nivel de dificultad",title="Dificultad",buttons=["Fácil","Medio","Difícil"])

    if eleccion == "Fácil":
        nivelProfundidad = 3
    elif eleccion == "Medio":
        nivelProfundidad = 4
    else: 
        nivelProfundidad = 5

    print(nivelProfundidad)

    while run:
        clock.tick(FPS)

        if game.turn == BLUE:
            #value, new_board = negamax(game.get_board(), 4, BLUE,-10000,10000, game) 
            value, new_board = minimaxBlue(game.get_board(), nivelProfundidad, BLUE,float('-inf'),float('inf'), game)
            game.ai_move(new_board)

        #elif game.turn == RED:
        #   value, new_board = minimaxRed(game.get_board(), 3, RED,float('-inf'),float('inf'), game)
        #   game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

        if game.winner() != None:
            if game.winner() == BLUE:
                pyautogui.alert(text="Las fichas AZULES ganan",title="Ganador",button="OK")
            else:
                pyautogui.alert(text="Las fichas ROJAS ganan",title="Ganador",button="OK")
            run = False
    
    pygame.quit()

main()