'''
Clase Punto:
    - Atributos:
        - color (char): Color del punto
        - inicial (bool): Indica si el punto es el inicial
        - coordenadas (tuple(int, int)): Coordenadas del punto
'''
class Punto:
    #Constructor
    def __init__(self, color, inicial, coordenadas):
        self.color = color
        self.inicial = inicial
        self.coordenadas = coordenadas
    
    def __str__(self)-> str:
        return self.color
    
    def getColor(self) -> str:
        return self.color
    
    def getInicial(self) -> bool:
        return self.inicial
    
    def getCoordenadas(self) -> tuple:
        return self.coordenadas
    
    def setColor(self, color: str):
        self.color = color
        
    def setInicial(self, inicial: bool):
        self.inicial = inicial
        
    def setCoordenadas(self, coordenadas: tuple):
        self.coordenadas = coordenadas
    