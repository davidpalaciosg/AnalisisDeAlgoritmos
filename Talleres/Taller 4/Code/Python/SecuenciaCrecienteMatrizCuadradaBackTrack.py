def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()


def secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j, M, B):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A):
        return 0

    if M[i][j] != 0:
        return M[i][j]

    q = 1
    sup, inf, izq, der = 0, 0, 0, 0
    # Fila superior
    if i > 0:
        if A[i][j]+1 == A[i-1][j]:
            sup = 1 + \
                secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i-1, j, M, B)
            B[i][j] = (i-1, j)

    # Fila inferior
    if i < len(A)-1:
        if A[i][j]+1 == A[i+1][j]:
            inf = 1 + \
                secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i+1, j, M, B)
            B[i][j] = (i+1, j)
    # Columna izquierda
    if j > 0:
        if A[i][j]+1 == A[i][j-1]:
            izq = 1 + \
                secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j-1, M, B)
            B[i][j] = (i, j-1)
    # Columna derecha
    if j < len(A)-1:
        if A[i][j]+1 == A[i][j+1]:
            der = 1 + \
                secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j+1, M, B)
            B[i][j] = (i, j+1)

    q = max(sup, inf, izq, der)
    M[i][j] = q
    return M[i][j]

def secuenciaCrecienteEnMatriz(A):
    #Crear tabla de memoizacion y backtracking
    M = [[0 for i in range(len(A))] for j in range(len(A))]
    B = [[(0, 0) for i in range(len(A))] for j in range(len(A))]
    q = 1
    # Casos base
    for i in range(len(A)):
        for j in range(len(A)):
            B[i][j] = (i, j)

    pos_actual = (0, 0)
    for i in range(len(A)):
        for j in range(len(A)):
            q = max(q, secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j, M, B))
            #Obtener la posicion de la secuencia mas larga
            if q == M[i][j]:
                pos_actual = (i, j)

    #Backtracking
    resultado = []
    #Mientras no llegue a la posición inicial
    while pos_actual != B[pos_actual[0]][pos_actual[1]]:
        resultado.append(A[pos_actual[0]][pos_actual[1]])
        pos_actual = B[pos_actual[0]][pos_actual[1]]
        
    #Agregar la posición inicial
    resultado.append(A[pos_actual[0]][pos_actual[1]])
    
    return resultado

A = [[10, 16, 15, 12],
     [9, 8, 7, 13],
     [2, 5, 6, 14],
     [3, 4, 1, 11]]

print(secuenciaCrecienteEnMatriz(A))