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

    def entropia(self,k):
        entropia=0
        cats=self.cat_total()
        n,o=self.cuenta_iguales(k,cats)
        #print("N y O")
        #print(n)
        #print(o)
        for i in range(len(cats[k])):
            if n[i]!=0 and o[i]!=0: 
                entropia+= ((-1)*((n[i]+o[i])/100))*((n[i]/(n[i]+o[i]))*math.log((n[i]/(n[i]+o[i])), 2)+(o[i]/(n[i]+o[i]))*math.log((o[i]/(n[i]+o[i])), 2))
            elif n[i]==0: 
                entropia+= ((-1)*((n[i]+o[i])/100))*((o[i]/(n[i]+o[i]))*math.log((o[i]/(n[i]+o[i])), 2))
            elif o[i]==0:
                entropia+= ((-1)*((n[i]+o[i])/100))*((n[i]/(n[i]+o[i]))*math.log((n[i]/(n[i]+o[i])), 2))
        return entropia
    
    def cat_total(self):
        cat_tot = []
        for i in range(len(self.nombres)):
            cat_tot.append(self.categorias(self.nombres[i]))
        return cat_tot

    def cuenta_iguales(self,k,cats): 
        catN=[]
        catO=[]
        dt = self.x.loc[self.x.Fertilidad == "O",:]
        dt2 = self.x.loc[self.x.Fertilidad == "N",:]
        for i in range(len(cats[k])):
            n=len(dt.loc[dt.iloc[:,k]== cats[k][i],:])
            catN.append(n)
            o=len(dt2.loc[dt2.iloc[:,k] == cats[k][i],:])
            catO.append(o)
        return catN, catO

    def categorias(self,columna):
        categorias=[]
        for i in self.x[columna]: 
            if i not in categorias: 
                categorias.append(i)        
        return categorias 
    
os.chdir("C:\\Users\\memon\\Downloads")
nombres=["Estacion", "Edad", "Enfermedades", "Accidente", "Cirugia", "Fiebre", "Alcohol", "Fumador", "Inactivo", "Fertilidad"]
datos=pd.read_csv('fertility_Diagnosis.txt', header=None, names=nombres)
#print(datos)
arbol=arbolDeClasificacion(datos, nombres)
a=arbol.cat_total()
n,o=arbol.cuenta_iguales(0,a)
for i in range(len(a)-1):
    print(arbol.entropia(i))








