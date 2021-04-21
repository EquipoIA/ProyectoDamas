import pygame

#Grid
WIDTH,HEIGHT = 800,800
ROWS,COLS = 8,8
SQUARE_SIZE = WIDTH//COLS

#rgb
BLACK = (0,0,0)
BLUE = (60, 39, 173)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTBLUE = (80,184,231)
LIGHTRED = (255,82,82)
GREY = (128,128,128)
GREEN = (181,229,80)

CROWN = pygame.transform.scale(pygame.image.load("GUI/assets/crown2.png"),(45,25))
