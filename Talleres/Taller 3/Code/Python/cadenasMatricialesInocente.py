import math
def cadenasMatricialesAux(D,i,j):
    if i==j:
        return 0
    
    q = math.inf
    for k in range (i,j):
        left = cadenasMatricialesAux(D,i,k)
        right = cadenasMatricialesAux(D,k+1,j)
        v = left+right+(D[i-1]*D[k]*D[j])  
        #Hallar el menor           
        if v < q:
            q = v
    return q

D = [10,100,5,50]
r = cadenasMatricialesAux(D,0,len(D)-2)
print(r)
