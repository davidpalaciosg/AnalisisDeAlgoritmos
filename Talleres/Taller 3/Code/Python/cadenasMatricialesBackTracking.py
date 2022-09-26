import math
import pprint


def imprimirMatriz(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end="\t")
        print()
        
#Agregar parentesis con backtracking
def agregarParentesis(B,i,j):
    #Si está en la diagonal imprime Ai 
    if i == j:
        return "A"+str(i+1)
    else:
        #Si no está en la diagonal significa que tiene operaciones pendientes
        q = B[i][j]
        left = agregarParentesis(B,i,q)
        right = agregarParentesis(B,q+1,j)
        return "( "+left+" "+right+" )"
    
def cadenasMatricialesAux(D):
    n = len(D) - 1
    M = [[0 for x in range(n)] for y in range(n)]
    B = [[-1 for x in range(n)] for y in range(n)]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            q = math.inf
            m = 0
            for k in range(i, j):
                left = M[i][k]
                right = M[k+1][j]
                v = left + right + (D[i-1]*D[k]*D[j])
                if v < q:
                    q = v
                    m = k
            M[i][j] = q
            B[i][j] = m
    
    return M, B


D = [10,100,5,50,250,15]
# Crear M
M, B = cadenasMatricialesAux(D)
r= M[0 ][ len(D)-2 ]
print("M: ")
imprimirMatriz(M)
print("B: ")
imprimirMatriz(B)
print(r)
print(agregarParentesis(B,0,len(B)-1))
