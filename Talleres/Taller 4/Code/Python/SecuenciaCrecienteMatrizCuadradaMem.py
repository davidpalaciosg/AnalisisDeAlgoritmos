def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def secuenciaCrecienteEnMatrizCuadradaMem(A, i,j, M):
    if M[i][j]!=0:
        return M[i][j] 
     
    q = 1
    #Fila superior
    if i>0:
        if A[i][j]+1 == A[i-1][j]:
            q = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i-1, j, M)
            
    #Fila inferior
    if i<len(A)-1:
        if A[i][j]+1 == A[i+1][j]:
            q = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i+1, j, M)
    #Columna izquierda
    if j>0:
        if A[i][j]+1 == A[i][j-1]:
            q = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i, j-1, M)
    #Columna derecha
    if j<len(A)-1:
        if A[i][j]+1 == A[i][j+1]:
            q = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i, j+1, M)
    M[i][j] = q
    return M[i][j]
     

A = [[10, 16, 15, 12],
     [9, 8, 7, 13],
     [2, 5, 6, 14],
     [3, 4, 1, 11]]

q= -9999999
M = [[0 for i in range(len(A))] for j in range(len(A))]

for i in range(len(A)):
    for j in range(len(A)):
        result = secuenciaCrecienteEnMatrizCuadradaMem(A, i, j, M)
        if result > q:
            q = result
            
print(q)
printMatrix(M)




