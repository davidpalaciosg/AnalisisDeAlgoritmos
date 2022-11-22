'''
Proyecto final Análisis de algoritmos
Presentado por:
    - David Enrique Palacios García: david_palacios@javeriana.edu.co
    - Karen Sofía Coral Godoy: corallg ksofia@javeriana.edu.co
    
Profesor:
    Leonardo Flórez Valencia

Manual de Uso:
    En una terminal, ejecutar el comando:
        python Main.py
'''
import sys
import FlowFree as FlowFree

def menu()->int:
    print("Bienvenido a Flow Free")
    print("Digite el número del tablero que desea resolver")
    print("0. Tablero 5x5_1")
    print("1. Tablero 5x5_2")
    print("2. Tablero 6x6_1")
    print("3. Tablero 6x6_2")
    print("4. Tablero 7x7_1")
    print("5. Tablero 7x7_2")
    print("6. Tablero 8x8_1")
    print("7. Tablero 8x8_2")
    print("8. Tablero 9x9_1")
    print("9. Tablero 9x9_2")
    opcion = int(input("Digite el número del tablero que desea resolver: "))
    return opcion


def main():
    flowfree = FlowFree.FlowFree()
    opcion = menu()
    if opcion<0 or opcion>9:
        print("Opción no válida, intentelo de nuevo")
        sys.exit()
    
    #Actualizar controlador
    archivo = flowfree.listaArchivos[opcion]
    flowfree.archivo = archivo
    flowfree.tablero.leerDatosDesdeArchivo(archivo)
    flowfree.tablero.filas = flowfree.tablero.datos.shape[0]
    flowfree.tablero.columnas = flowfree.tablero.datos.shape[1]
    print(flowfree.tablero)
    
    print("Hallando solución...")
    solucion = flowfree.encontrarSolucion()
    print("Solución encontrada")
    print(solucion)
    
main()