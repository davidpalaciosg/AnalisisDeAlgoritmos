from math import pow
#Convert an integer number into binary list
def DecimalToBinary(n):
    binary=[]
    while n !=0:
        binary.insert(0,str(n%2))
        n //= 2
    return binary

#Invert a chain given a list begin and end
def InvertChain(S):
    if len(S)==1:
        return S[0]
    result  = []
    for i in range (len(S)-1,-1,-1):
        result.append(S[i])
    return result

#Convert a list of binary into an integer
def BinaryToDecimal(numero_binario):
    decimal = 0
    i=0
    inverted = InvertChain(numero_binario)
    for i in range(len(inverted)):
        p = int(pow(int(inverted[i])*2,i))
        decimal = decimal + p
    return decimal

n = 345
print(n)
binario= DecimalToBinary(n)
print("original", binario)
binarioInverso = InvertChain(binario)
print("inverso", binarioInverso)
decimal= BinaryToDecimal(binarioInverso)
print(decimal)