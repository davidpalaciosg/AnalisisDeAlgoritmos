'''
Primera entrega de proyecto: Análisis de algoritmos
    Interfaz: Flow Free
Profesor: Leonardo Flórez Valencia

Estudiantes:
    - David Enrique Palacios García (david_palacios@javeriana.edu.co)
    - Karen Sofía Coral Godoy (corallg_ksofia@javeriana.edu.co)

Manual de uso:
    - Para ejecutar el programa: abrir una terminal y escribir el comando:
        python3 FlowFree.py
'''
import os

from matplotlib.pyplot import table
from Punto import Punto
from Tablero import Tablero

# Limpia la consola
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion que imprime la bienvenida
def Bienvenida():
    print("Primer Proyecto: Analisis de algoritmos")
    print("Profesor: Leonardo Florez Valencia")
    print("Desarrollado por: David Palacios y Sofía Coral")
    print("Bienvenido a Flow Free")
    print("Dimension del tablero-> numero de Puntos")
    print(" 5. 5x5 ->                  4 puntos" )
    print(" 6. 6x6 ->                  5 puntos" )
    print(" 7. 7x7 ->                  6 puntos" )
    print(" 8. 8x8 ->                  7 puntos" )
    print(" 9. 9x9 ->                  8 puntos" )

#Funcion que imprime el menu de opciones
def menu()->int:
    print("Opciones:")
    print("1. Realizar movimiento")
    print("2. Deshacer movimiento")
    print("3. Ver puntos originales")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

#Interfaz para realizar movimiento
def realizarMovimiento_Int(dimension:int, tablero:Tablero)->bool:
    try:
        #Obtener las coordenadas del punto inicial
        f1 = int(input("Ingrese la fila del punto inicial: "))
        c1 = int(input("Ingrese la columna del punto inicial: "))
        if f1 < 0 or c1 < 0 or f1 >= dimension or c1 >= dimension:
            print("ERROR: Coordenadas de punto inicial no válidas")
            return False
        
        # Obtener las coordenadas del punto final
        f2 = int(input("Ingrese la fila del punto final: "))
        c2 = int(input("Ingrese la columna del punto final: "))
        if f2 < 0 or c2 < 0 or f2 >= dimension or c2 >= dimension:
            print("ERROR: Coordenadas de punto final no válidas")
            return False
    except:
        print("ERROR: Coordenadas no válidas")
        
    puntoInicial = tablero.getPunto(f1, c1)
    puntoFinal = tablero.getPunto(f2, c2)
    
    if tablero.realizarMovimiento(puntoInicial, puntoFinal):
        print("Movimiento realizado exitosamente")
        return True
    
    return False

# Interfaz para deshacer movimiento
def deshacerMovimiento_Int(dimension:int, tablero:Tablero)->bool:
    try:
        #Obtener las coordenadas del punto inicial
        f1 = int(input("Ingrese la fila del punto inicial a remover: "))
        c1 = int(input("Ingrese la columna del punto inicial a remover: "))
        if f1 < 0 or c1 < 0 or f1 >= dimension or c1 >= dimension:
            print("ERROR: Coordenadas de punto inicial no válidas")
            return False
        
        # Obtener las coordenadas del punto final
        f2 = int(input("Ingrese la fila del punto final a remover: "))
        c2 = int(input("Ingrese la columna del punto final a remover: "))
        if f2 < 0 or c2 < 0 or f2 >= dimension or c2 >= dimension:
            print("ERROR: Coordenadas de punto final no válidas")
            return False
    except:
        print("ERROR: Coordenadas no válidas")
        
    puntoInicial = tablero.getPunto(f1, c1)
    puntoFinal = tablero.getPunto(f2, c2)
    if tablero.deshacerMovimiento(puntoInicial, puntoFinal):
        print("Movimiento deshecho exitosamente")
        return True
    
    return False
    
# Función principal del programa
def main():
    Bienvenida()
    #Obtener la dimension del tablero
    dimension = 0
    while dimension < 5 or dimension > 9:
        dimension = int(input("Ingrese la dimension del tablero: "))
        if dimension < 5 or dimension > 9:
            print("ERROR: Dimension no válida")
            
    #Crear el tablero
    numPuntos = dimension - 1
    tablero = Tablero(dimension)
    
    # Mientras no se gane
    while not tablero.verificarVictoria():
        #Seleccionar una opcion
        opcion = 0
        while opcion != 4:
            #limpiarConsola()
            tablero.imprimirTablero()
            opcion = menu() 
            if opcion == 1:
                #Realizar movimiento
                realizarMovimiento_Int(dimension,tablero)
            elif opcion == 2:
                #Deshacer movimiento
                deshacerMovimiento_Int(dimension,tablero)
            elif opcion==3:
                #Imprimir puntos originales
                tablero.imprimirPuntosOriginales()
            else:
                print("ERROR: Opcion no valida")

# Llamadp a la función principal
main()