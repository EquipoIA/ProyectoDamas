class Pieza(object):
    def __init__(self, color, rey=False):
        self.color = color
        self.rey = rey

class Jugador(object):
    def __init__(self, tipo, color, nivel):
        self.tipo = tipo #si es persona o IA
        self.color = color
        self.nivel = nivel #profundidad de busqueda


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
        for j in range(8):
            if(tablero[i][j]==1):
                nueva_pieza = Pieza('n')
                tablero[i][j] = nueva_pieza
            elif(tablero[i][j]==-1):
                nueva_pieza = Pieza('r')
                tablero[i][j] = nueva_pieza
    return tablero

def imprime_tablero(tablero):
    for i in range(8):
        for j in range(8):
            if(tablero[i][j]==0):
                print("0", end=" ")
            else:
                print(tablero[i][j].color, end=" ")
        print("\n")

def movimientos_posibles(tablero, jugador):
    movimientos = []
    for m in range(8):
        for n in range(8):
            if tablero[m][n] != 0 and tablero[m][n].color == jugador.color:
                if puede_capturar([m, n], [m+1, n+1], [m+2, n+2], tablero) == True:
                     movimientos.append([m, n, m+2, n+2])
                if puede_capturar([m, n], [m-1, n+1], [m-2, n+2], tablero) == True:
                     movimientos.append([m, n, m-2, n+2])
                if puede_capturar([m, n], [m+1, n-1], [m+2, n-2], tablero) == True:
                     movimientos.append([m, n, m+2, n-2])
                if puede_capturar([m, n], [m-1, n-1], [m-2, n-2], tablero) == True:
                     movimientos.append([m, n, m-2, n-2])


    return movimientos


def puede_capturar(tablero,posInic,posInter,posFinal):
    pieza_inic = tablero[posInic[0]][posInic[1]]
    pieza_inter = tablero[posInter[0]][posInter[1]]
    #revisar si la posFinal es valida
    if posFinal[0] < 0 or posFinal[0] > 7 or posFinal[1] < 0 or posFinal[1] > 7:
        return False
    #revisar si la posFinal contiene una pieza
    if tablero[posFinal[0]][posFinal[1]]!=0:
        return False
    #revisar si la posInter tiene una ficha
    if pieza_inter==0:
        return False
    #Si la pieza inicial es roja, revisar si puede capturar
    if pieza_inic.color == 'r':
        if pieza_inic.rey == False and posFinal[0]>posInic[0]:
            return False
        if pieza_inter.color == 'r':
            return False
        return True
    else:
        if pieza_inic.rey == False and posFinal[0]<posInic[0]:
            return False
        if pieza_inter.color == 'n':
            return False
        return True

def puede_moverse(posInic,posFinal,tablero):
