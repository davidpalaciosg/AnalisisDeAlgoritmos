'''
Clase Camino:
    - Atributos:
        -c (int): color del camino [1,9]
        -i (int): fila de inicio del camino
        -j (int): columna de inicio del camino
        -k (int): fila de fin del camino
        -j (int): columna de fin del camino
        
'''
class Camino:
    c:int = None
    i:int = None
    j:int = None
    k:int = None
    j:int = None
    def __init__(self,c:int,i:int,j:int,k:int,l:int) -> None:
        self.c = c
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        
    def __str__(self) -> str:
        cadena = "Color: "+str(self.c)+" Inicio: ("+str(self.i)+","+str(self.j)+") Fin: ("+str(self.k)+","+str(self.l)+")"
        return cadena