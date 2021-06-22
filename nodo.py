class NodoCabecera:
    def __init__(self,fila=None,columna=None,color=None):
        self.fila=fila
        self.columna=columna
        self.color=color
        self.arriba=None
        self.abajo=None
        self.izquierda=None
        self.derecha=None

class NodoPivote:
    def __init__(self,fila=None,columna=None,color=None):
        self.fila=fila
        self.columna=columna
        self.color=color
        self.derechaP=None
        self.abajoP=None

class Nodo:
    def __init__(self,fila=None,columna=None,color=None):
        self.fila=fila
        self.columna=columna
        self.color=color
        self.arriba=None
        self.abajo=None
        self.derecha=None
        self.izquierda=None

class contenidoNodo:
    def __init__(self,fila,columna,color):
        self.fila=fila
        self.columna=columna
        self.color=color
