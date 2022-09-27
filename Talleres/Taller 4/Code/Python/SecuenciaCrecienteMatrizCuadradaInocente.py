def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def secuenciaCrecienteEnMatrizCuadrada(A, i,j):  
    q = 1
    #Fila superior
    if i>0:
        if A[i][j]+1 == A[i-1][j]:
            q = 1 + secuenciaCrecienteEnMatrizCuadrada(A, i-1, j)
            
    #Fila inferior
    if i<len(A)-1:
        if A[i][j]+1 == A[i+1][j]:
            q = 1 + secuenciaCrecienteEnMatrizCuadrada(A, i+1, j)
    #Columna izquierda
    if j>0:
        if A[i][j]+1 == A[i][j-1]:
            q = 1 + secuenciaCrecienteEnMatrizCuadrada(A, i, j-1)
    #Columna derecha
    if j<len(A)-1:
        if A[i][j]+1 == A[i][j+1]:
            q = 1 + secuenciaCrecienteEnMatrizCuadrada(A, i, j+1)
    return q
     

A = [[10, 16, 15, 12],
     [9, 8, 7, 13],
     [2, 5, 6, 14],
     [3, 4, 1, 11]]

q= -9999999
for i in range(len(A)):
    for j in range(len(A)):
        result = secuenciaCrecienteEnMatrizCuadrada(A, i, j)
        if result > q:
            q = result
            
print(q)




