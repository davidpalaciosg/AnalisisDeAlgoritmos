import math
import pprint
def printMatrix(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end="\t")
        print()

def cadenasMatricialesAux(D):
    n = len(D)
    M = [[0 for x in range(len(D))] for y in range(len(D))]
    B = [[0 for x in range(len(D))] for y in range(len(D))]
    
    for i in range (n-2, -1 ,-1):
        for j in range(i+1, n):
            q = math.inf
            m = 0
            for k in range (i,j):
                left = M[i][k]
                right =M[k+1][j]
                v = left + right + (D[i-1]*D[k]*D[j])
                if v < q:
                    q = v
                    m = k  
            M[i][j] = q
            B[i][j] = m
    return M , B    

D = [10,100,5,50]

#Crear M
M , B = cadenasMatricialesAux(D)
print("M: ")
printMatrix(M)
print("B: ")
printMatrix(B)






