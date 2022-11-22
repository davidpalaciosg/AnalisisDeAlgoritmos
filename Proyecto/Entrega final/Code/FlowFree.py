'''
Clase FlowFree:
    - Atributos:
        -tablero (Tablero): tablero del juego
        -colores (list): lista de colores
        -listaArchivos (list): lista de archivos de tableros
        -archivo (str): archivo de tablero a utilizar         
    - Métodos:
        -crearListaArchivos(self): Crea la lista de archivos de tableros
        -crearCaminos(self): Crea todos los caminos posibles del tablero
        -encontrarSolucion(self): Busca la solución del tablero mediante la combinatoria de los caminos
        -validarCaminos(self,caminos:list): Valida que una combinatoria de caminos sea válida
        -validarTableroPrueba(self,tableroPrueba:pd.DataFrame): Valida que el tablero de prueba sea correcto

'''
import pandas as pd
import Tablero as Tablero
import Camino as Camino
import itertools
class FlowFree:
    tablero:Tablero = None
    colores:list = None
    listaArchivos:list = None
    archivo:str = None
    
    def __init__(self) -> None:
        self.tablero:Tablero = Tablero.Tablero()
        self.colores:list = [0,1,2,3,4,5,6,7,8,9]
        self.listaArchivos:list = self.crearListaArchivos()
        self.archivo:str = self.listaArchivos[0]
        
    def crearListaArchivos(self)->list:
        separador = "\\"
        cadena = "Tableros"+separador
        cadena5x5 = cadena+"5x5"+separador
        cadena6x6 = cadena+"6x6"+separador
        cadena7x7 = cadena+"7x7"+separador
        cadena8x8 = cadena+"8x8"+separador
        cadena9x9 = cadena+"9x9"+separador
        listaArchivos = [cadena5x5+"5x5_1.csv",
                              cadena5x5+"5x5_2.csv",
                              cadena6x6+"6x6_1.csv",
                              cadena6x6+"6x6_2.csv",
                              cadena7x7+"7x7_1.csv",
                              cadena7x7+"7x7_2.csv",
                              cadena8x8+"8x8_1.csv",
                              cadena8x8+"8x8_2.csv",
                              cadena9x9+"9x9_1.csv",
                              cadena9x9+"9x9_2.csv"]
        return listaArchivos
    
    #Valida que una combinatoria de caminos sea correcta
    def validarCaminos(self,caminos:list)->bool:
        #Copiar el tablero original
        tableroPrueba = self.tablero.datos.copy()
        #Recorrer los caminos
        for camino in caminos:
            color = camino.c
            i = camino.i
            j = camino.j
            k = camino.k
            l = camino.l
            
            #Si el camino es diagonal, no es válido
            if i!=k and j!=l:
                return False
            
            #Si algún camino se solapa con otro, no es válido
            if tableroPrueba[i][j] != 0:
                return False
            if tableroPrueba[k][l] != 0:
                return False
            
            #Asignar el color al camino
            tableroPrueba[i][j] = color
            tableroPrueba[k][l] = color
            
        #Validar el tablero
        return self.validarTableroPrueba(tableroPrueba)
    
    #Valida si un tablero de prueba es correcto      
    def validarTableroPrueba(self,tableroPrueba:pd.DataFrame)->bool:
        #Recorrer el tablero
        for i in range(self.tablero.filas):
            for j in range(self.tablero.columnas):
                #Si el tablero tiene un 0, no es válido
                if tableroPrueba[i][j] == 0:
                    return False
        return True
    
    #Crea todos los caminos posibles del tablero
    def crearCaminos(self)->list:
        caminos = []
        #Crear todos los caminos posibles
        for i in range(self.tablero.filas):
            for j in range(self.tablero.columnas):
                for k in range(self.tablero.filas):
                    for l in range(self.tablero.columnas):
                        for color in self.colores:
                            caminoNuevo = Camino.Camino(color,i,j,k,l)
                            caminos.append(caminoNuevo)
        return caminos
    
    #Encuentra la solución del tablero verificando todas las combinaciones posibles
    def encontrarSolucion(self)->list:
        caminos = self.crearCaminos()
        for r in range(1,len(caminos)+1):
            for combinacion in itertools.combinations(caminos,r):
                if self.validarCaminos(combinacion):
                    return combinacion
            
        