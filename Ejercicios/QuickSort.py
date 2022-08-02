import random

def Partition(S, p, r):
    x= S[r]
    i= p-1
    for j in range (p, r):
        if S[j] <= x:
            i+=1
            S[i], S[j]= S[j], S[i]
        #end if
    #end for
    S[i+1], S[r]= S[r], S[i+1]
    return i+1
#end def

def RandomizedPartition(S, p, r):
    i= random.randint(p,r)
    S[r], S[i]= S[i], S[r]
    return Partition (S, p, r)
#end def

def QuickSort_Aux(S, p, r):
    if p < r:
        q=RandomizedPartition(S, p, r)
        QuickSort_Aux(S, p, q-1)
        QuickSort_Aux(S, q+1, r)
    #end if
#end def

def QuickSort(S):
    QuickSort_Aux(S, 0, len(S)-1)
#end def

S= [5, 2, 3, 6, 1, 0]

print (S)
QuickSort(S)
print(S)