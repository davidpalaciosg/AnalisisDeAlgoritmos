"""
Taller 1 Análisis de Algoritmos PUJ 2022-3
Autores:
    - Sofía Coral
    - David Palacios
Profesor:
    - Leonardo Flórez

Manual de uso:

En una terminal, ejecutar el siguiente comando:
    $ python taller1.py
"""
from random import seed
from random import randint
import timeit

# seed random number generator
seed(1)

def createRandomList(n):
    """
    Crea una lista de n elementos aleatorios entre 0 y 1000000
    """
    list =[]
    for _ in range(n):
        list.append(randint(0,1000000))
    return list

def classicBubbleSort(list):
    """
    Retorna una lista de n elementos usando el algoritmo de burbuja y 
    el tiempo de ejecución en segundos que tarda en ordenarla
    """
    start = timeit.default_timer()
    for i in range(len(list)):
        for j in range(len(list)-1):
           if list[j+1]<list[j]:
               aux = list[j]
               list[j] = list[j+1]
               list[j+1] = aux
    stop = timeit.default_timer()
    
    return list, stop-start

def improvedBubbleSort(list):
    """
    Retorna una lista de n elementos usando el algoritmo de burbuja mejorado y 
    el tiempo de ejecución en segundos que tarda en ordenarla
    """
    start = timeit.default_timer()
    for i in range(len(list)):
        for j in range(len(list)-i):
           if list[j+1]<list[j]:
               aux = list[j]
               list[j] = list[j+1]
               list[j+1] = aux
    stop = timeit.default_timer()
    
    return list, stop-start

def insertionSort(list):
    """
    Retorna una lista de n elementos usando el algoritmo de inserción y 
    el tiempo de ejecución en segundos que tarda en ordenarla
    """
    start = timeit.default_timer()
    for j in range(1, len(list)):
        key = list[j]
        i = j-1
        while 0<i and key < list[i]:
                list[i+1] = list[i]
                i -= 1
        list[i+1] = key
        
    stop = timeit.default_timer()
    return list, stop-start

