import math
def cadenasMatricialesAux(D,i,j):
    if i == j:
        return 0
    else:
        q = math.inf
        for k in range (i,j):
            left = cadenasMatricialesAux(D,i,k)
            right = cadenasMatricialesAux(D,k+1,j)
            v = left+right+(D[i]*D[k]*D[j])
            
            #Hallar el menor           
            if v < q:
                q = v
        return q

D = [5,4,6,8,10]
r = cadenasMatricialesAux(D,0,len(D)-1)
print(r)
