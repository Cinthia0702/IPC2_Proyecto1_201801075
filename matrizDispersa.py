import os
from nodo import*

class EncabezadoX:
    def __init__(self) :
        self.cabezaX=None
        self.colaX=None
        self.abajoX=None
        self.izquierdaX=None
        self.derechaX=None
        self.tamaño=0

    def insertarX(self,coordenadaX,coordenadaY,color): 
        nuevoNodo=NodoCabecera(coordenadaX,coordenadaY,color)     
        if self.cabezaX == None:
            # la cola de la lista es igual a la cabeza de la lista
            self.cabezaX=self.colaX=nuevoNodo
        else:
            if self.verificarCoordenadasX(coordenadaX)==True:
                pass
            else:
                nodoAux=self.colaX
                self.colaX=nuevoNodo
                nuevoNodo.izquierda=nodoAux
                nodoAux.derecha=nuevoNodo
                nuevoNodo.abajo=nuevoNodo
                self.ordenarCabecerasX(coordenadaX,coordenadaY,color)
        self.tamaño+=1

    def mostarX(self):
        nuevoNodo=self.cabezaX
        while nuevoNodo!=None:
            print(nuevoNodo.fila, end='<->')
            nuevoNodo=nuevoNodo.derecha
        print('None')

    def verificarCoordenadasX(self,coordenadaX):
        nodoActual=self.cabezaX
        if nodoActual==None:
            print('Lista vacia')
            return False
        else:
            if self.cabezaX==self.colaX:
                if coordenadaX in nodoActual.fila:
                    print('Existe nodo')
                    return True
            else:
                while nodoActual!=None:
                    if coordenadaX in nodoActual.fila:
                        print('Existe nodo')
                        return True
                    nodoActual=nodoActual.derecha
            return False
    
    def ordenarCabecerasX(self,coordenadaX,coordenadaY,color):
        nodoNuevo=NodoCabecera(coordenadaX,coordenadaY,color)
        nodoActual=self.cabezaX
        if self.cabezaX==None:
            print('Lista vacia')
        else:
            while nodoActual != None:
                nodoNuevo=nodoActual.derecha
                while nodoNuevo !=None:
                    if nodoNuevo.fila < nodoActual.fila:
                        nodoAux=nodoActual.fila
                        nodoActual.fila=nodoNuevo.fila
                        nodoNuevo.fila=nodoAux
                    nodoNuevo=nodoNuevo.derecha
                nodoActual=nodoActual.derecha

    def buscarCoordenadaX(self,coordenandaX):
        nodoActual=self.cabezaX
        while nodoActual !=None:
            if coordenandaX == nodoActual.fila:
                print(nodoActual.fila)
                return nodoActual
            nodoActual=nodoActual.derecha
        
class EncabezadoY:
    def __init__(self):
        self.cabezaY=None
        self.colaY=None
        self.arribaY=None
        self.abajoY=None
        self.derechaY=None
        self.tamaño=0

    def insertarY(self,coordenadaX,coordenadaY,color): 
        nuevoNodo=NodoCabecera(coordenadaX,coordenadaY,color)     
        if self.cabezaY == None:
            # la cola de la lista es igual a la cabeza de la lista
            self.cabezaY=self.colaY=nuevoNodo
        else:
            if self.verificarCoordenadasY(coordenadaY)==True:
                pass
            else:
                nodoAux = self.colaY
                self.colaY = nuevoNodo
                nuevoNodo.arriba = nodoAux
                nodoAux.abajo = nuevoNodo
                nuevoNodo.derecha = nuevoNodo
                self.ordenarCabecerasY(coordenadaX,coordenadaY,color)
        self.tamaño+=1

    def mostarY(self):
        nuevoNodo=self.cabezaY
        while nuevoNodo!=None:
            print(nuevoNodo.columna)
            nuevoNodo=nuevoNodo.abajo
        print('None')

    def verificarCoordenadasY(self,coordenada):
        nodoActual=self.cabezaY
        if nodoActual==None:
            print('Lista vacia')
            return False
        else:
            if self.cabezaY==self.colaY:
                if coordenada in nodoActual.columna:
                    print('Existe nodo')
                    return True
            else:
                while nodoActual!=None:
                    if coordenada in nodoActual.columna:
                        print('Existe nodo')
                        return True
                    nodoActual=nodoActual.abajo
            return False
            
    def ordenarCabecerasY(self,coordenadaX,coordenadaY,color):
        nodoNuevo=NodoCabecera(coordenadaX,coordenadaY,color)
        nodoActual=self.cabezaY
        if self.cabezaY==None:
            print('Lista vacia')
        else:
            while nodoActual != None:
                nodoNuevo=nodoActual.abajo
                while nodoNuevo !=None:
                    if nodoNuevo.columna < nodoActual.columna:
                        nodoAux=nodoActual.columna
                        nodoActual.columna=nodoNuevo.columna
                        nodoNuevo.columna=nodoAux
                    nodoNuevo=nodoNuevo.abajo
                nodoActual=nodoActual.abajo

    def buscarCoordenadaY(self,coordenandaY):
        nodoActual=self.cabezaY
        while nodoActual != None:
            if nodoActual.columna==coordenandaY:
                print('Si existe en y ',nodoActual.columna)
                return nodoActual
            nodoActual=nodoActual.abajo

class nodoPivote:
    def __init__(self):
        self.cabezaP=None
        self.derecha=None
        self.abajo=None
        self.encabezadoX=EncabezadoX()
        self.encabezadoY=EncabezadoY()
        self.tamaño=0
    
    def insertarAPivote(self,coordenadaXP,coordenadaYP,color):
        nodoRaiz=NodoPivote(coordenadaXP,coordenadaYP,color)
        self.cabezaP=nodoRaiz
        nodoRaiz.derechaP=self.encabezadoX.insertarX(coordenadaXP,coordenadaYP,color)
        nodoRaiz.abajoP=self.encabezadoY.insertarY(coordenadaXP,coordenadaYP,color)
        self.tamaño+=1

    def mostrarPivote(self):
        nuevoNodoX=self.encabezadoX.cabezaX
        while nuevoNodoX!=None:
            print(nuevoNodoX.fila,end='<->')
            nuevoNodoX=nuevoNodoX.derecha
        print('None')
        
        nuevoNodoY=self.encabezadoY.cabezaY
        while nuevoNodoY!=None:
            print(nuevoNodoY.columna)
            nuevoNodoY=nuevoNodoY.abajo
        print('None')
    
    def buscarCabeceras(self,coordenadaX, coordenadaY):
        nodoActual=self.cabezaP
        if nodoActual == None:
            print('Lista vacia')
        else:
            while nodoActual != None:
                if nodoActual.fila == coordenadaX and nodoActual.columna == coordenadaY:
                    print('Si existe en x ', nodoActual.fila)
                    print('Si existe en y ', nodoActual.columna)
                    return True
                nodoActual=nodoActual.derechaP
    
    def insertarAMatriz(self,coordenadaX,coordenadaY,color):
        if self.buscarCabeceras(coordenadaX,coordenadaY) == True:
            print('Se agrego',color)

    def Graficar(self):
        nodoActual=self.cabezaP
        nodoActual2=self.cabezaP
        file=open('Matriz.dot',mode='w',encoding="utf-8")
        diagrama='digraph G{\n'
        diagrama+='rankdir=LR;'
        nodo=1
        nodo2=1
        diagrama+=('Raiz[label=\"x=0 y=0\nRaiz\",shape=circle,group=0];\n')
        while nodoActual.derechaP!=None:
            diagrama+='Nodo'
            diagrama+=str(nodo)
            diagrama+='[shape=circle,label=\"x='
            diagrama+=nodoActual.raiz.fila
            diagrama+=' y=0\n'
            diagrama+=nodoActual.raiz.color
            diagrama+='\",group='
            diagrama+=nodoActual.raiz.fila+'];\n'    
            nodoActual=nodoActual.derechaP
            nodo=nodo+1
        diagrama+='Nodo'
        diagrama+=str(nodo)
        diagrama+='[shape=circle,label=\"x='
        diagrama+=nodoActual.raiz.fila
        diagrama+=' y=0\n'
        diagrama+=nodoActual.raiz.color
        diagrama+='\",group='
        diagrama+=nodoActual.raiz.fila+'];\n'    
        while nodoActual2.derechaP !=None:
            diagrama+='Raiz->Nodo'
            diagrama+=str(nodo2)
            diagrama+='->Nodo'
            diagrama+=str(nodo2+1)
            nodoActual2=nodoActual2.derechaP
            nodo2=nodo+1
        diagrama+='}'
        file.write(diagrama)
        file.close()
        os.system('dot -Tpng Matriz.dot -o Matriz.png')
        os.system("Matriz.png") 
