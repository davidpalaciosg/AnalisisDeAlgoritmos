'''
Clase Tablero:
    - Atributos:
        - numPuntos (int): Número de puntos del tablero
        - dimension (int): Dimensiones del tablero
        - cantMovimientos (int): Cantidad de movimientos realizados
        - porcentaje (float): Porcentaje de llenado del tablero
        - matriz (list(list(Punto))): Matriz de puntos
        - caminos (list(Camino)): Lista de caminos
        
    - Métodos:
        - __init__(self, dimension)
        - imprimirTablero(self)
        - crearMatriz(self, numPuntos, dimension)
        - validarMovimiento(self, PuntoInicial, PuntoFinal)
        - realizarMovimiento(self, PuntoInicial, PuntoFinal)
        - calcularPorcentaje(self)
        - getPunto(self, fila, columna)
        - getCamino(self, color)
        - verificarVictoria(self)
'''
from sympy import prime
from Camino import Camino
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
        self.caminos = []
        #Crear los caminos iniciales
        for color in self.colores:
            self.caminos.append(Camino(color))
        
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
            #Hacia la derecha (Filas derecha)
            if coordInicial[1] < coordFinal[1]:
                for c in range(coordInicial[1]+1, coordFinal[1]+1):
                    if self.matriz[coordInicial[0]][c].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                return "FD"
            #Hacia la izquierda (Filas izquierda)
            else:
                for c in range(coordInicial[1]-1, coordFinal[1]-1, -1):
                    if self.matriz[coordInicial[0]][c].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                return "FI"
        
        #Si está en la misma columna (VERTICAL)
        if PuntoInicial.getCoordenadas()[1] == PuntoFinal.getCoordenadas()[1]:
            #Hacia abajo (Columnas inferior)
            if coordInicial[0] < coordFinal[0]:
                for f in range(coordInicial[0]+1, coordFinal[0]+1):
                    if self.matriz[f][coordInicial[1]].getColor() != " ":
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                return "CI"
            #Hacia arriba (Columnas superior)
            else:
                for f in range(coordInicial[0]-1, coordFinal[0]-1, -1):
                    if self.matriz[f][coordInicial[1]].getColor() != " ": 
                        print("ERROR: Hay puntos entre los dos")
                        return "N"
                return "CS"
            
        return "N"
    
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
        
        #Crear Camino
        camino = Camino(PuntoInicial.getColor())
        camino.puntos.append(PuntoInicial)
        
        #Hacia la derecha
        if tipoMov == "FD":
            for c in range(coordInicial[1]+1, coordFinal[1]+1):
                self.matriz[coordInicial[0]][c].setColor(PuntoInicial.getColor())
                camino.puntos.append(self.matriz[coordInicial[0]][c])
        
        #Hacia la izquierda
        elif tipoMov == "FI":
            for c in range(coordInicial[1], coordFinal[1]-1, -1):
                self.matriz[coordInicial[0]][c].setColor(PuntoInicial.getColor())
                camino.puntos.append(self.matriz[coordInicial[0]][c])
                
        #Hacia abajo       
        elif tipoMov == "CI":
            for f in range(coordInicial[0], coordFinal[0]+1):
                self.matriz[f][coordInicial[1]].setColor(PuntoInicial.getColor())
                camino.puntos.append(self.matriz[f][coordInicial[1]])
                
        #Hacia arriba
        elif tipoMov == "CS":         
            for f in range(coordInicial[0], coordFinal[0]-1, -1):
                self.matriz[f][coordInicial[1]].setColor(PuntoInicial.getColor())
                camino.puntos.append(self.matriz[f][coordInicial[1]])
        
        #Finalizar camino
        camino.puntos.append(PuntoFinal)
        #Actualizar caminos
        indexColor = self.colores.index(PuntoInicial.getColor())
        self.caminos[indexColor] = camino
        
        #Actualizar el porcentaje
        self.porcentaje = self.calcularPorcentaje()
        
        #Actualizar la cantidad de movimientos
        self.cantMovimientos+=1
        
        #Actualizar el punto inicial
        PuntoInicial.setUltimo(False)
        PuntoFinal.setUltimo(True)
        
        
        return True  
 
    def validarDeshacerMovimiento(self, PuntoInicial: Punto, PuntoFinal: Punto)->str:
        
        #Si los puntos son iguales, no se puede deshacer el movimiento
        if PuntoFinal.getCoordenadas() == PuntoInicial.getCoordenadas():
            print("ERROR: El punto final es el mismo que el inicial")
            return "N"
        
        if PuntoInicial.getColor() == " ":
            print("ERROR: El punto inicial está vacío")
            return "N"
        
        if PuntoFinal.getColor() == " ":
            print("ERROR: El punto final está vacío")
            return "N"
        
        if PuntoFinal.getColor() != PuntoInicial.getColor():
            print("ERROR: Los puntos DEBEN ser del mismo color")
            return "N"
        
        if not PuntoInicial.getUltimo():
            print("ERROR: El punto inicial DEBE SER el ultimo por donde se continuo el camino")
            return "N"
        
        if PuntoFinal.getOriginal():
            print("ERROR: El punto final no puede ser un punto original")
            return "N"
        
        #Validar camino entre los dos puntos
        coordInicial = PuntoInicial.getCoordenadas()
        coordFinal = PuntoFinal.getCoordenadas()
        
        #Si está en la misma fila (HORIZONTAL)
        if coordInicial[0] == coordFinal[0]:
            #Hacia la derecha (Filas derecha)
            if coordInicial[1] < coordFinal[1]:
                for c in range(coordInicial[1]+1, coordFinal[1]+1):
                    if self.matriz[coordInicial[0]][c].getColor() != PuntoInicial.getColor():
                        print("ERROR: Camino no valido")
                        return "N"                        
                return "FD"
            #Hacia la izquierda (Filas izquierda)
            else:
                for c in range(coordInicial[1]-1, coordFinal[1]-1, -1):
                    if self.matriz[coordInicial[0]][c].getColor() != PuntoInicial.getColor():
                        print("ERROR: Camino no valido")
                        return "N"
                return "FI"
        #Si está en la misma columna (VERTICAL)
        if coordInicial[1] == coordFinal[1]:
            #Hacia abajo (Columna abajo)
            if coordInicial[0] < coordFinal[0]:
                for f in range(coordInicial[0]+1, coordFinal[0]+1):
                    if self.matriz[f][coordInicial[1]].getColor() != PuntoInicial.getColor():
                        print("ERROR: Camino no valido")
                        return "N"
                return "CI"
            #Hacia arriba (Columna arriba)
            else:
                for f in range(coordInicial[0]-1, coordFinal[0]-1, -1):
                    if self.matriz[f][coordInicial[1]].getColor() != PuntoInicial.getColor():
                        print("ERROR: Camino no valido")
                        return "N"
                return "CS"
        return "N"
    
    def deshacerMovimiento(self, PuntoInicial:Punto, PuntoFinal: Punto)->bool:
        #Validar si se puede deshacer el movimiento
        tipoMovDeshacer = self.validarDeshacerMovimiento(PuntoInicial, PuntoFinal)
        if tipoMovDeshacer == "N":
            return False
        
        indiceColor = self.colores.index(PuntoInicial.getColor())
                    
        #Actualizar el tablero
        coordInicial = PuntoInicial.getCoordenadas()
        coordFinal = PuntoFinal.getCoordenadas()
        
        #Obtener Camino
        camino = self.caminos[indiceColor]
        camino.puntos.pop()
        
        fFinal, cFinal = coordFinal
        #Hacia la derecha
        if tipoMovDeshacer == "FD":
            for c in range(coordInicial[1], coordFinal[1]+1):
                self.matriz[coordInicial[0]][c].setColor(" ")
                camino.puntos.pop()
                fFinal, cFinal = coordInicial[0], c+1
        
        #Hacia la izquierda
        elif tipoMovDeshacer == "FI":
            for c in range(coordInicial[1], coordFinal[1]-1, -1):
                self.matriz[coordInicial[0]][c].setColor(" ")
                camino.puntos.pop()
                fFinal, cFinal = coordInicial[0], c-1
                
        #Hacia abajo       
        elif tipoMovDeshacer == "CI":
            for f in range(coordInicial[0], coordFinal[0]+1):
                self.matriz[f][coordInicial[1]].setColor(" ")
                camino.puntos.pop()
                fFinal, cFinal = f+1, coordInicial[1]
                
        #Hacia arriba
        elif tipoMovDeshacer == "CS":         
            for f in range(coordInicial[0], coordFinal[0]-1, -1):
                self.matriz[f][coordInicial[1]].setColor(" ")
                camino.puntos.pop()
                fFinal, cFinal = f-1, coordInicial[1]
        
        #Finalizar camino
        camino.puntos.pop()
        #Actualizar caminos
        self.caminos[indiceColor] = camino
        
        #Actualizar el porcentaje
        self.porcentaje = self.calcularPorcentaje()
        
        #Actualizar la cantidad de movimientos
        self.cantMovimientos-=1
        
        #Actualizar el punto inicial
        PuntoInicial.setUltimo(False)
        PuntoFinal.setUltimo(False)
        
        #Actualizar el punto final
        self.matriz[fFinal][cFinal].setUltimo(True)
        
        #Si el punto final restante es de los originales, se desactiva el camino
        if self.matriz[fFinal][cFinal].getOriginal():
            self.caminosActivos[indiceColor] = False
        
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
              
    def verificarVictoria(self)->bool:
        
        correctos=[]
        for camino in self.caminos:
            if len(camino.puntos)>0:
                primerPunto:Punto = camino.puntos[0]
                ultimoPunto:Punto = camino.puntos[-1]
                
                #Si son iguales, el camino no es correcto
                coordInicial = primerPunto.getCoordenadas()
                coordFinal = ultimoPunto.getCoordenadas()
                if coordInicial == coordFinal:
                    correctos.append(False)
                #Si alguno de los dos no es original, el camino no es correcto
                elif not (primerPunto.getOriginal() and ultimoPunto.getOriginal()):
                    correctos.append(False)
                else:
                    correctos.append(True)
                
        #Si todos los caminos son correctos, se gana
        if correctos.count(True)==self.numPuntos:
            #Si el porcentaje es 100, se gana
            if self.porcentaje == 100:
                return True
        return False
    
    def imprimirPuntosOriginales(self):
        print("Puntos originales:")
        f, c = 0,0
        #Imprimir la fila de ayuda
        print(" ", end=" ")
        for f in range (self.dimension):
            print(f, end = " ")
        print()
        
        for fp in range(self.dimension):
            #Imprimir la columna de ayuda
            print(c, end = " ")
            c+=1
            for cp in range(self.dimension):
                
                punto:Punto = self.matriz[fp][cp]
                
                if punto.getOriginal():
                    print(punto.getColor(), end=" ")
                else:
                    print(" ", end=" ")
            print()
            
    def reiniciarTablero(self):
        for f in range(self.dimension):
            for c in range(self.dimension):
                punto:Punto = self.matriz[f][c]
                if not (punto.getOriginal):
                    punto.setColor(" ")
                    punto.setUltimo(False)
                