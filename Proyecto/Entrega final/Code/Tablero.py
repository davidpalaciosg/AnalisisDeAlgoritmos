'''
Clase Tablero:
    - Atributos:
        -filas (int): cantidad de filas del tablero
        -columnas (int): cantidad de columnas del tablero
        -datos (Pandas DataFrame): datos del tablero
    - Métodos:
        - leerDatosDesdeArchivo(self,archivo:str): Lee los datos del tablero desde un archivo csv
'''
import pandas as pd
class Tablero:
    filas:int = None
    columnas:int = None
    datos:pd.DataFrame = None
    
    def __init__(self,filas:int,columnas:int) -> None:
        self.filas = filas
        self.columnas = columnas
        self.datos = pd.DataFrame(0,index=range(filas),columns=range(columnas))
    
    def __init__(self) -> None:
        self.filas = 0
        self.columnas = 0
        self.datos = pd.DataFrame(0,index=range(self.filas),columns=range(self.columnas))
    
    def __str__(self) -> str:
        cadena = '\n'
        cadena += 'Tablero de ' + str(self.filas) + 'x' + str(self.columnas) + '\n'
        cadena += str(self.datos)
        return cadena    
    
    def leerDatosDesdeArchivo(self,archivo:str) -> None:
        self.datos = pd.read_csv(archivo,header=None, sep=' ')