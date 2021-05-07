from pandas import DataFrame
import pandas as pd
import os
import math 
from math import log 

class Nodo: 
    def __init__(self):
        self.value=None
        self.value=None 
        self.childs=None

class arbolDeClasificacion:
    def __init__(self, x, nombres):
        self.x=x
        self.nombres=nombres
        #self.categoriasC=list(set())

    def entropia(self,columna):
        cat=self.categorias(columna)
        numInst=self.numInstancias(cat,columna)
        entropia=0
        n,o=self.cuenta_iguales(columna)
        for i in range(len(cat)):
            entropia+= ((-1)*(numInst[i]/sum(numInst)))*((n[i]/numInst[i])*math.log((n[i]/numInst[i]), 2)+(o[i]/numInst[i])*math.log((o[i]/numInst[i]), 2))
        return entropia
    
    def cuenta_iguales(self, columna): 
        catN=[]
        catO=[]
        dt = self.x.loc[datos.Fertilidad == "O",:]
        dt2 = self.x.loc[datos.Fertilidad == "N",:]
        for i in range(len(categorias)):
            n=len(dt.loc[dt.Edad == categorias[i],:])
            catN.append(n)
            o=len(dt2.loc[dt2.Edad == categorias[i],:])
            catO.append(o)
        return catN, catO

            
    def categorias(self,columna):
        categorias=[]
        for i in self.x[columna]: 
            if i not in categorias: 
                categorias.append(i)        
        return categorias 

    def numInstancias(self, categorias, columna): 
        vecesIns=[]
        for i in categorias: 
            vecesIns.append(list(self.x[columna]).count(i))
        return vecesIns
    
os.chdir("C:\\Users\\memon\\Downloads")
nombres=["Estación", "Edad", "Enfermedades", "Accidente", "Cirugía", "Fiebre", "Alcohol", "Fumador", "Inactivo", "Fertilidad"]
datos=pd.read_csv('fertility_Diagnosis.txt', header=None, names=nombres)
print(datos)
arbol=arbolDeClasificacion(datos, nombres)      
categorias=(arbol.categorias("Edad"))
print(categorias)
print("lel")
num=arbol.numInstancias(categorias, "Edad")
n,o=arbol.cuenta_iguales("Edad")
print(n)
print(o)
print(sum(n)+sum(o))
print(num)
entropia=arbol.entropia("Edad")
print(entropia)






