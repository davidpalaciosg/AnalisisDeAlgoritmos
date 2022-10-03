'''
Clase Camino:
    - Atributos:
        - puntos (list(Punto)): Lista de puntos que forman un camino en el tablero
        - color (str): Color del camino
'''
class Camino:
    def __init__(self, color):
        self.puntos = []
        self.color = color
        
    def __str__(self)-> str:
        cadena ="["
        for punto in self.puntos:
            cadena += str(punto) + ", "
        cadena = cadena[:-2]
        cadena += "]"
        return cadena
    def print(self):
        print(self.__str__())
