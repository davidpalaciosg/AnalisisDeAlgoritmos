def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def secuenciaCrecienteEnMatrizCuadradaMem(A, i,j, M):
    if i<0 or i>=len(A) or j<0 or j>=len(A):
        return 0
    
    if M[i][j]!=-1:
        return M[i][j] 
    
    q = 1
    sup, inf, izq, der = 0,0,0,0
    #Fila superior
    if i>0:
        if A[i][j]+1 == A[i-1][j]:
            sup = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i-1, j, M)
            
    #Fila inferior
    if i<len(A)-1:
        if A[i][j]+1 == A[i+1][j]:
            inf = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i+1, j, M)
    #Columna izquierda
    if j>0:
        if A[i][j]+1 == A[i][j-1]:
            izq = 1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i, j-1, M)
    #Columna derecha
    if j<len(A)-1:
        if A[i][j]+1 == A[i][j+1]:
            der =  1 + secuenciaCrecienteEnMatrizCuadradaMem(A, i, j+1, M)
    
    q = max(sup, inf, izq, der)
    M[i][j] = q
    return M[i][j]
     

A = [[10, 16, 15, 12],
     [9, 8, 7, 13],
     [2, 5, 6, 14],
     [3, 4, 1, 11]]

q= -9999999
M = [[-1 for i in range(len(A))] for j in range(len(A))]

for i in range(len(A)):
    for j in range(len(A)):
        if M[i][j]==-1:
            secuenciaCrecienteEnMatrizCuadradaMem(A, i, j, M)
        q = max(q, M[i][j])
                    
print(q)
printMatrix(M)




