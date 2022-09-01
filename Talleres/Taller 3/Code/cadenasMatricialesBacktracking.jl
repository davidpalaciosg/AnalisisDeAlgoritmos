## =========================================================================
## @author David Enrique Palacios-Garcia (david_palacios@javeriana.edu.co)
## @author Karen Sofia Coral Godoy (corallg ksofia@javeriana.edu.co) 
## =========================================================================
"""
Manual de uso:
Ejecutar en el shell o cmd-> julia cadenasMatricialesBacktracking.jl #MatricesIter1 #MatricesIter2 #MatricesIter3 
#MatricesIter4 #MatricesIter5 #MatricesIter6 #MatricesIter7 #MatricesIter8 #MatricesIter9 #MatricesIter10

Params:
Debido a que el experimento consta de 10 iteraciones, el i va desde 1 hasta 10
- #MatricesIter_i: número de matrices a multiplicar en la Iteracion i
"""
function agregarParentesis(B,i,j)
  #Si está en la diagonal imprime Ai 
  if i == j
    print("A"*string(i)*" ")
  else
    print("( ")
    q = B[i,j]
    agregarParentesis(B,i,q)
    agregarParentesis(B,q+1,j)
    print(") ")
  end
end

function cadenasMatriciales(D)
  n = length(D) - 1
  M = [0 for i = 1:n,j=1:n]
  B = [-1 for i = 1:n,j=1:n]
  
  for i in n-1:-1:1
    for j in i+1:n
      q = Inf
      m = 1
      for k in i:j-1
        left = M[i,k]
        right = M[k+1,j]
        #Realizar ajuste de casilla negativa
        x = 0
        if i-1 == 0 
          x = D[length(D)]
        else
          x = D[i-1]
        end
        v = left+right+(x*D[k]*D[j])
        if v < q
          q = v
          m = k
        end
      end
      M[i,j] = q
      B[i,j] = m
    end
  end
  return M, B
end

function imprimirCadenasMatriciales(muestra)
  for i=1:10
    println("Iteracion: ", i)
    println("Numero de matrices: ", muestra[i])
    D=[]
    for i=1:muestra[i]+1
      random = rand(1:100)
      push!(D, random)
    end
    println("D: ")
    println(D)
    M, B = cadenasMatriciales(D)
    r = M[1,length(D)-1]
    println("M: ")
    println(M)
    println("B: ")
    println(B)
    println("Multiplicaciones optimas: ", r)
    agregarParentesis(B,1,size(B)[1])
    println()
    println("-----------------------")
  end
end

muestra=[]
for i=1:10
  push!(muestra, parse(Int64, ARGS[i]))
end
imprimirCadenasMatriciales(muestra)

