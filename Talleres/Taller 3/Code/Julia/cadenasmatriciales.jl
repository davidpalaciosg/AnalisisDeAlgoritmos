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

function imprimirCadenasMatriciales(D)
  M, B = cadenasMatriciales(D)
  r = M[1,length(D)-1]
  println("M: ")
  println(M)
  println("B: ")
  println(B)
  println(r)
  agregarParentesis(B,1,size(B)[1])
  println()
end

D = [10, 100, 5, 50]
imprimirCadenasMatriciales(D)
