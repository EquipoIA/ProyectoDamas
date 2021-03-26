import pygame

newGame=True
loggedIn=False
miniGame=False

black=(0,0,0)
blue=(60, 39, 173)
white=(255,255,255)
red=(255,0,0)
greyBackground=(203, 206, 203)

# This sets the WIDTH and HEIGHT of each grid location
width=65
height=65
radius=30

margin=0# This sets the margin between each cell
xDistanceFromEdge=220
gameBoard=[[None]*8 for _ in range(8)]  # Proper initialization.
windowSize=[960, 640]

pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Draughts Game")
done = False
clock = pygame.time.Clock()

# Added helper function.
def square_colour(row, col):
    """ Determine colour of game board square from its position. """
    return white if (row + col) % 2 == 0 else black  # Makes upper-left corner white.

def boardGui(black,white):
    for boardRow in range(8):
        for boardColumn in range(8):
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])

def piecesGameBoard(gameBoard):
    if newGame:
        newGameBoard(gameBoard)

def newGameBoard(gameBoard):
    gameBoard[:] = [[None]*8 for _ in range(8)]  # Empty the game board.

    for x in range(8):
        for y in range(8):
            if square_colour(x, y) == black:
                if y in range(3):
                    gameBoard[x][y]="NormalBlack"
                if y in range(5,8):
                    gameBoard[x][y]="NormalRed"

    drawPieces(gameBoard,black,red)

def drawPieces(gameBoard,black,red):
    for x in range(8):
        for y in range(8):
            xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
            yCoordinate=(margin+height) * y + margin+33
            if gameBoard[x][y]=="NormalBlack":
                pygame.draw.circle(screen,blue,(xCoordinate,yCoordinate),radius)
                # Draw a white outline around edge of black pieces so they are visible
                # when placed on black game board squares.
                pygame.draw.circle(screen,blue,(xCoordinate,yCoordinate),radius, 1)
            if gameBoard[x][y]=="KingBlack":
                pygame.draw.circle(screen,blue,(xCoordinate,yCoordinate),radius)
                #-----put letter k in the middle-----#
            if gameBoard[x][y]=="NormalRed":
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
            if gameBoard[x][y]=="KingRed":
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
                #----put letter k in the middle---#

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height+margin)

    screen.fill(greyBackground)
    boardGui(black,white)
    piecesGameBoard(gameBoard)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()