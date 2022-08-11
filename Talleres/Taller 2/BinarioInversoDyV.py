#Convert an integer number into binary list
def DecimalToBinary(numero_decimal):
    binario = []
    while numero_decimal != 0:
        binario.insert(0, str(numero_decimal % 2))
        numero_decimal //= 2
    return (binario)

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
	for posicion, digito_string in enumerate(numero_binario[::-1]):
		decimal += int(digito_string) * 2 ** posicion
	return decimal

n = 345
print(n)
binario= DecimalToBinary(n)
print(binario)
binarioInverso = InvertChain(binario,0,len(binario)-1)
print(binarioInverso)
decimal= BinaryToDecimal(binarioInverso)
print(decimal)