import math
import pprint

def imprimirMatriz(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end="\t")
        print()

def cadenasMatricialesAux(D,i,j,M):
    if i == j:
        M[i][j]=0
        
    q = math.inf
    #Si no se ha calculado
    if M[i][j]==math.inf:    
        for k in range (i,j):
            left = cadenasMatricialesAux(D,i,k,M)
            right = cadenasMatricialesAux(D,k+1,j,M)
            v = left+right+(D[i-1]*D[k]*D[j])
                
            #Hallar el menor           
            if v < q:
                q = v
                    
        M[i][j] = q
    return M[i][j]

D = [10,100,5,50]

#Crear M
M = [[math.inf for x in range(len(D)-1)] for y in range(len(D)-1)]
r = cadenasMatricialesAux(D,0,len(D)-2, M)
print("M: ")
imprimirMatriz(M)
print(r)


