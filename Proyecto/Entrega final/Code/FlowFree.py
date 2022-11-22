'''
Clase FlowFree:
    - Atributos:
        -tablero (Tablero): tablero del juego
        -colores (list): lista de colores
        -listaArchivos (list): lista de archivos de tableros
        -archivo (str): archivo de tablero a utilizar         
    - Métodos:
        -crearListaArchivos(self): Crea la lista de archivos de tableros
        -crearCaminos(self): Crea la combinatoria de caminos del juego
        -validarCaminos(self,caminos:list): Valida que los caminos sean correctos
'''
import pandas as pd
import Tablero as Tablero
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
        