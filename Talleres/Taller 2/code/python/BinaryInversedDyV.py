from math import pow
#Convert an integer number into binary list
def DecimalToBinary(n):
    binary = []
    while n != 0:
        binary.insert(0, str(n % 2))
        n //= 2
    return (binary)

#Invert a chain given a list begin and end
def InvertChain(S,l,r):
    if l==r:
        return S[l]

    q = (l+r)//2
    left = InvertChain(S,l,q)
    right= InvertChain(S,q+1,r)
    result=[]

    #SWAP
    for i in range(len(right)):
        result.append(right[i])
    for i in range(len(left)):
        result.append(left[i])
    return result

#Convert a list of binary into an integer
def BinaryToDecimal(numero_binario):
    decimal = 0
    i=0
    inverted = InvertChain(numero_binario,0,len(numero_binario)-1)
    for i in range(len(inverted)):
        p = int(pow(int(inverted[i])*2,i))
        decimal = decimal + p
    return decimal

print("Binary Inversed DyV")
n = 345
binary= DecimalToBinary(n)
print("Original:", n, binary)
binarioInverso = InvertChain(binary,0,len(binary)-1)
decimal= BinaryToDecimal(binarioInverso)
print("Inverso:", decimal, binarioInverso)