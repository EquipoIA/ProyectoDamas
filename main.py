class Pieza(object):
    def __init__(self, color, rey=False):
        self.color = color
        self.rey = rey

def tablero_inicial():
    tablero = [
	[ 0, 1, 0, 1, 0, 1, 0, 1],
	[ 1, 0, 1, 0, 1, 0, 1, 0],
	[ 0, 1, 0, 1, 0, 1, 0, 1],
	[ 0, 0, 0, 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0, 0, 0, 0],
	[-1, 0,-1, 0,-1, 0,-1, 0],
	[ 0,-1, 0,-1, 0,-1, 0,-1],
	[-1, 0,-1, 0,-1, 0,-1, 0]]

    for i in range(8):
        for j in range(9):
            if(tablero[i][j]==1):
                nueva_pieza = Pieza('negro')
                tablero[i][j] = nueva_pieza
            elif(tablero[i][j]==-1):
                nueva_pieza = Pieza('rojo')
                tablero[i][j] = nueva_pieza
    return tablero
