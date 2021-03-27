from copy import deepcopy

class Pieza(object):
    def __init__(self, color, rey=False):
        self.color = color
        self.rey = rey

class Jugador(object):
    def __init__(self, tipo, color, nivel):
        self.tipo = tipo #si es persona o IA
        self.color = color
        self.nivel = nivel #profundidad de busqueda

global jugador1 = Jugador('persona','r',2)
global jugador2 = Jugador('ia','n',3)

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

#Define los movimientos posibles que puede hacer un jugador dado un tablero
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
    #si en ningun movimiento puede capturar al oponente, se mueve normalmente
    if len(movimientos)==0:
        for m in range(8):
            for n in range(8):
                if tablero[m][n] != 0 and tablero[m][n].color == jugador.color:
                    if puede_moverse([m, n], [m+1, n+1], tablero) == True: 
                        movimientos.append([m, n, m+1, n+1])
                    if puede_moverse([m, n], [m-1, n+1], tablero) == True: 
                        movimientos.append([m, n, m-1, n+1])
                    if puede_moverse([m, n], [m+1, n-1], tablero) == True: 
                        movimientos.append([m, n, m+1, n-1])
                    if puede_moverse([m, n], [m-1, n-1], tablero) == True: 
                        movimientos.append([m, n, m-1, n-1])
    return movimientos


def puede_capturar(posInic,posInter,posFinal,tablero):
    pieza_inic = tablero[posInic[0]][posInic[1]]
    
    #revisar si la posFinal es valida
    if posFinal[0] < 0 or posFinal[0] > 7 or posFinal[1] < 0 or posFinal[1] > 7:
        return False
    #revisar si la posFinal contiene una pieza
    if tablero[posFinal[0]][posFinal[1]]!=0:
        return False
    #revisar si la posInter tiene una ficha
    pieza_inter = tablero[posInter[0]][posInter[1]]
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
    pieza_inic = tablero[posInic[0]][posInic[1]]
    #revisar si la posFinal es valida
    if posFinal[0] < 0 or posFinal[0] > 7 or posFinal[1] < 0 or posFinal[1] > 7:
        return False
    #revisar si posFinal esta vacia
    if tablero[posFinal[0]][posFinal[1]] != 0:
        return False
    #Si la pieza es rey, entonces ya se puede mover sin restriccion
    if pieza_inic.rey:
        return True
    #pieza roja
    elif pieza_inic.color == 'r':
        if posFinal[0]>posInic[0]:
            return False
        return True
    #pieza negra
    else:
        if posFinal[0]<posInic[0]:
            return False
        return True
#hacer el movimiento en el tablero 
def mover_pieza(posInic,posFinal,tablero):
    tablero[posFinal[0]][posFinal[1]] = tablero[posInic[0]][posInic[1]]
    tablero[posInic[0]][posInic[1]] = 0

    #checar si la pieza movida se convierte en rey
    if posFinal[0]==0 and tablero[posFinal[0]][posFinal[1]].color =='r':
        tablero[posFinal[0]][posFinal[1]].rey = True
    if posFinal[0]==7 and tablero[posFinal[0]][posFinal[1]].color =='n':
        tablero[posFinal[0]][posFinal[1]].rey = True
    
    #checar si capturamos una ficha para eliminarla
    if (posInic[0]-posFinal[0])%2==0:
        tablero[(posInic[0]+posFinal[0])/2][(posInic[1]+posFinal[1])/2] = 0 


def heuristica(tablero, jugador):
    valor = 0
    for i in range(8):
        for j in range(8):
            pos = tablero[i][j]
            if pos != 0:
                if pos.color == jugador.color:
                    if pos.rey:
                        valor += 2
                    else:
                        valor += 1
                else:
                    if pos.rey:
                        valor -= 2
                    else:
                        valor -= 1
    return valor

def perdio_juego(tablero,jugador):
    if len(movimientos_posibles(t,jugador)) != 0:
        return False
    for i in range(8):
        for j in range(8):
            if tablero[i][j] != 0 and tablero[i][j].color == jugador.color:
                return False
    return True

def negamax(tablero,nivel,jugador,alpha,beta):
    global mejor_movimiento
    if nivel==0 or perdio_juego(jugador1) or perdio_juego(jugador2):
        return heuristica(tablero,jugador)
    movimientos = movimientos_posibles(tablero,jugador)
    for i in range(len(movimientos)):
        copia_tablero = deepcopy(tablero)
        mover_pieza((movimientos[i][0],movimientos[i][1]),(movimientos[i][2],movimientos[i][3]),copia_tablero)
        if jugador == jugador1:
            jugador = jugador2
        else:
            jugador = jugador1
        valor_temp = -negamax(copia_tablero,nivel-1,-beta,-alpha,jugador)
        if valor_temp > alpha:
            if nivel=0:
                mejor_movimiento = (movimientos[i][0],movimientos[i][1]),(movimientos[i][2],movimientos[i][3])
            alpha = valor_temp
        if alpha >= beta:
            break
    return alpha




#pruebas
t = tablero_inicial()
imprime_tablero(t)
mover_pieza([5,0],[4,1],t)
imprime_tablero(t)

print(movimientos_posibles(t,jugador1))
print(heuristica(t,jugador1))
