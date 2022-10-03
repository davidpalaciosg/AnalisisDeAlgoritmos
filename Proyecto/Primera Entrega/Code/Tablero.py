'''
Clase Tablero:
    - Atributos:
        - numPuntos (int): Número de puntos del tablero
        - dimension (int): Dimensiones del tablero
        - cantMovimientos (int): Cantidad de movimientos realizados
        - porcentaje (float): Porcentaje de llenado del tablero
        - matriz (list(list(Punto))): Matriz de puntos
        
    - Métodos:
        - __init__(self, dimension)
        - imprimirTablero(self)
        - crearMatriz(self, numPuntos, dimension)
        - validarMovimiento(self, PuntoInicial, PuntoFinal)
        - realizarMovimiento(self, PuntoInicial, PuntoFinal)
        - calcularPorcentaje(self)
'''
from Punto import Punto
from random import randint

'''
Colores: 
    R = Rojo,
    V = Verde,
    A = Azul,
    N = Negro,
    M = Morado,
    C = Cyan,
    B = Blanco,
    G = Gris,
    T = Turquesa
'''



class Tablero:
    #Constructor
    def __init__(self, dimension: int):
        self.colores = ["R","V","A","N","M","C","B","G","T"]
        self.caminosActivos =[False for x in range(len(self.colores))]
        
        self.dimension = dimension
        self.numPuntos = dimension - 1
        self.cantMovimientos = 0
        
        self.matriz = self.crearMatriz(self.numPuntos, dimension)
        self.porcentaje = self.calcularPorcentaje()
    def imprimirTablero(self):
        print()
        print("Dimension: ", self.dimension, "x", self.dimension)
        print("Cantidad de movimientos: ", self.cantMovimientos)
        print("Porcentaje: %.2f" %self.porcentaje, "%")
        print("Tablero actual: ")
        f, c = 0,0
        #Imprimir la fila de ayuda
        print(" ", end=" ")
        for f in range (self.dimension):
            print(f, end = " ")
        print()
            
        for fila in self.matriz:  
            #Imprimir la columna de ayuda
            print(c, end = " ")
            c+=1
            
            #Imprimir los puntos
            for punto in fila:
                print(punto, end=" ")
            print()
            
    def crearMatriz(self, numPuntos: int, dimension: int) -> list:
        #M = [[0 for x in range(n)] for y in range(n)]
        
        matriz = []
        
        #Crear matriz vacía
        for f in range (dimension):
            list = []
            for c in range (dimension):
                nuevo = Punto(" ", False, (f,c))    
                list.append(nuevo)
            matriz.append(list)
       
        
        #Crear coordenadas iniciales
        coordenadas = []
        terminar = False
        while not terminar:
            #Generar coordenadas
            f = randint(0, numPuntos)
            c = randint(0, numPuntos)
                        
            #Validar que no se repitan
            if (f,c) not in coordenadas:
                coordenadas.append((f,c))
                                   
            #Validar que se hayan generado los puntos iniciales
            if len(coordenadas) == numPuntos*2:
                terminar = True
            
        color = 0
        #Actualizar matriz
        for c in range(0, len(coordenadas), 2):
            #Obtener coordenadas
            c1 = coordenadas[c]
            c2 = coordenadas[c+1]
            
            #Obtener los puntos de esas coordenadas
            p1:Punto = matriz[c1[0]][c1[1]]
            p2:Punto = matriz[c2[0]][c2[1]]
            
            #Actualizar los puntos
            p1.setColor(self.colores[color])
            p1.setOriginal(True)
            p1.setUltimo(True)
            p2.setColor(self.colores[color])
            p2.setOriginal(True)
            p2.setUltimo(True)
            
            #Siguiente color
            color+=1
        
        return matriz

    def validarMovimiento(self, PuntoInicial: Punto, PuntoFinal: Punto)->str:
        
        #Si los puntos son iguales, no se puede realizar el movimiento
        if PuntoFinal.getCoordenadas() == PuntoInicial.getCoordenadas():
            print("ERROR: El punto final es el mismo que el inicial")
            return "N"
        
        #Si el punto inicial está vacío, no se puede realizar el movimiento
        if PuntoInicial.getColor() == " ":
            print("ERROR: El punto inicial está vacío")
            return "N"
        
        #Si el punto inicial es de los originales y existe un camino activo, no se puede realizar el movimiento  
        if PuntoInicial.getOriginal() and self.caminosActivos[self.colores.index(PuntoInicial.getColor())]:
            print("ERROR: Existe un camino activo con ese color")
            return "N"
        
        #Si el punto final no está vacío, no se puede realizar el movimiento
        if PuntoFinal.getColor() != " ":
            print("ERROR: El punto final no está vacío")
            return "N"
        
        #Si el punto inicial no es el último por donde se continuó el camino, no se puede realizar el movimiento
        if not PuntoInicial.getUltimo():
            print("ERROR: El camino activo se encuentra en otro punto")
            return "N"
        
        coordInicial = PuntoInicial.getCoordenadas()
        coordFinal = PuntoFinal.getCoordenadas()
        
        #Verificar que no haya puntos entre los dos
        #Si está en la misma fila (HORIZONTAL)
        if PuntoInicial.getCoordenadas()[0] == PuntoFinal.getCoordenadas()[0]:
            #Hacia la derecha
            if coordInicial[1] < coordFinal[1]:
                for c in range(coordInicial[1]+1, coordFinal[1]+1):
                    if self.matriz[coordInicial[0]][c].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
            #Hacia la izquierda
            else:
                for c in range(coordInicial[1]-1, coordFinal[1]-1, -1):
                    if self.matriz[coordInicial[0]][c].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                    
            return "F"
        
        #Si está en la misma columna (VERTICAL)
        if PuntoInicial.getCoordenadas()[1] == PuntoFinal.getCoordenadas()[1]:
            #Hacia abajo
            if coordInicial[0] < coordFinal[0]:
                for f in range(coordInicial[0]+1, coordFinal[0]+1):
                    if self.matriz[f][coordInicial[1]].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
            #Hacia arriba
            else:
                for f in range(coordInicial[0]-1, coordFinal[0]-1, -1):
                    if self.matriz[f][coordInicial[1]].getColor() != " ": 
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                    
            return "C"
    
    def realizarMovimiento(self, PuntoInicial: Punto, PuntoFinal: Punto)->bool:
        
        #Validar el movimiento
        tipoMov = self.validarMovimiento(PuntoInicial, PuntoFinal)
        if tipoMov == "N":
            return False
        
        #Si el punto inicial es de los originales, se activa el camino
        if PuntoInicial.getOriginal():
            indice = self.colores.index(PuntoInicial.getColor())
            self.caminosActivos[indice] = True
        
        #Actualizar el tablero
        coordInicial = PuntoInicial.getCoordenadas()
        coordFinal = PuntoFinal.getCoordenadas()
        
        if tipoMov == "F":
            #Actualizar la fila
            #Hacia la derecha
            if coordInicial[1] < coordFinal[1]:
                for c in range(coordInicial[1], coordFinal[1]+1):
                    self.matriz[coordInicial[0]][c].setColor(PuntoInicial.getColor())
            #Hacia la izquierda
            else:
                for c in range(coordInicial[1], coordFinal[1]-1, -1):
                    print("Se agrega en:", coordInicial[0], c)
                    self.matriz[coordInicial[0]][c].setColor(PuntoInicial.getColor())
                    
        elif tipoMov == "C":
            #Actualizar la columna
            #Hacia abajo
            if coordInicial[0] < coordFinal[0]:
                for f in range(coordInicial[0], coordFinal[0]+1):
                    self.matriz[f][coordInicial[1]].setColor(PuntoInicial.getColor())
            #Hacia arriba
            else:
                for f in range(coordInicial[0], coordFinal[0]-1, -1):
                    self.matriz[f][coordInicial[1]].setColor(PuntoInicial.getColor())
        #Actualizar el porcentaje
        self.porcentaje = self.calcularPorcentaje()
        
        #Actualizar la cantidad de movimientos
        self.cantMovimientos+=1
        
        #Actualizar el punto inicial
        PuntoInicial.setUltimo(False)
        PuntoFinal.setUltimo(True)
        
        return True  
 
    def calcularPorcentaje(self)->float:
        total = self.dimension * self.dimension
        pintados = 0
        for f in range(self.dimension):
            for c in range(self.dimension):
                if self.matriz[f][c].getColor() != " ":
                    pintados+=1
        porcentaje = (pintados/total)*100
        return porcentaje
    
    def getPunto(self, f:int, c:int)->Punto:
        return self.matriz[f][c]          