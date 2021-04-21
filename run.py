import pygame
import pyautogui

from GUI.constants import *
from GUI.game import Game
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
        nivelProfundidad = 2
    elif eleccion == "Medio":
        nivelProfundidad = 4
    else: 
        nivelProfundidad = 6

    print(nivelProfundidad)

    while run:
        clock.tick(FPS)

        if game.turn == BLUE:
            value, new_board = minimaxBlue(game.get_board(), nivelProfundidad, BLUE,float('-inf'),float('inf'))
            if new_board != None:
                game.ai_move(new_board)
            else:
                pyautogui.alert(text="Las fichas Azules no tienen movimientos posibles",title="Ganador",button="OK")
                break
        
        ####################
        '''
        elif game.turn == RED:
           value, new_board = minimaxRed(game.get_board(), 2, RED,float('-inf'),float('inf'))
           game.ai_move(new_board)
        '''
        ####################
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
                break
            else:
                pyautogui.alert(text="Las fichas ROJAS ganan",title="Ganador",button="OK")
                break
            run = False
        #checar si red se quedo sin movimientos
        movs_red = get_all_moves(game.get_board(), RED)
        if movs_red == []:
            pyautogui.alert(text="Las fichas Rojas no tienen movimientos posibles",title="Ganador",button="OK")
            break
    
    pygame.quit()

main()
