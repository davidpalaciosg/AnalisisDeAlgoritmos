'''
Clase Punto:
    - Atributos:
        - color (char): Color del punto
        - original (bool): Indica si el punto es el original
        - coordenadas (tuple(int, int)): Coordenadas del punto
        - ultimo (bool): Indica si el punto es el ultimo marcado en el tablero
'''
class Punto:
    #Constructor
    def __init__(self, color, original, coordenadas):
        self.color = color
        self.original = original
        self.coordenadas = coordenadas
        self.ultimo=False
    
    def __str__(self)-> str:
        return self.color
    
    def getColor(self) -> str:
        return self.color
    
    def getOriginal(self) -> bool:
        return self.original
    
    def getCoordenadas(self) -> tuple:
        return self.coordenadas
    
    def setColor(self, color: str):
        self.color = color
        
    def setOriginal(self, original: bool):
        self.original = original
        
    def setCoordenadas(self, coordenadas: tuple):
        self.coordenadas = coordenadas
    def getUltimo(self):
        return self.ultimo
    
    def setUltimo(self,ultimo):
        self.ultimo=ultimo
    