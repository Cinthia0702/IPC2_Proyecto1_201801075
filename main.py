from matrizDispersa import*

if __name__=='__main__':
    #Revisar el tamaño del tablero con lo ingresado
    #Revisar el si ya existe en la matriz
    #Revisar porque en las filas se repite el numero
    listaCabeceraX=EncabezadoX()
    listaCabeceraY=EncabezadoY()
    pivote=nodoPivote()
    
    n=input('Ingrese la cantidad de filas: ')
    m=input('Ingrese la cantidad de columnas: ')
        
    for i in range(int(m)):
        for j in range(int(n)):
            coordenadaX=input('Ingrese coordenada en x: ')
            coordenadaY=input('Ingrese coordenada en y: ')
            color=input('Ingrese color: ')
            listaCabeceraX.insertarX(coordenadaX,coordenadaY,'')
            listaCabeceraY.insertarY(coordenadaX,coordenadaY,'')
            print('\nLas cabeceras son: \n')
            pivote.insertarAPivote(coordenadaX,coordenadaY,'')
            pivote.mostrarPivote()
            print('cabeceras')
            dato1=input('Ingrese un dato: ')
            dato2=input('Ingrese un dato: ')
            pivote.buscarCabeceras(dato1,dato2)
            print('\nLa matriz es: \n')
            pivote.insertarAMatriz(dato1,dato2,color)
    #pivote.Graficar()