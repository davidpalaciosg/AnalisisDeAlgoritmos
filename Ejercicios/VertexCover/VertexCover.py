'''
  User manual:
  On the terminal, type:
    python3 VertexCover.py <n> <p>
  where n is the number of vertex and p is the probability of an edge
  
'''
from CreateGraph import *
import itertools,copy

# Find an approximation of the vertex cover
def aproxVertexCover(vertex, matrix):
  C = []
  #Duplicate matrix
  E_aux = [[0 for i in range(len(vertex))] for j in range(len(vertex))]
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      E_aux[i][j] = matrix[i][j]
  
  #While the matrix is not empty
  while isMatrixEmpty(E_aux) == False:
    #Get a random edge
    i = random.randint(0, len(vertex) - 1)
    j = random.randint(0, len(vertex) - 1)
    value = E_aux[i][j]
    value2 = E_aux[j][i]
    if value > 0 or value2 > 0:
      if i not in C:
        C.append(i)
      
      #Remove edges on row i
      E_aux[i] = [0 for i in range(len(vertex))]
      #Remove edges on column i
      for k in range(len(vertex)):
        E_aux[k][i] = 0
      
  return C


#Verify if the combination of vertex cover all edges
def bruteForceVerification(c, vertex, matrix):
  matrixCopy = copy.deepcopy(matrix)
  for x in c:
    for i in range(len(vertex)):
      matrixCopy[i][x]=0
      matrixCopy[x][i]=0

  s = 0
  for i in range (len(vertex)):
    for j in range (len(vertex)):
      s+=matrixCopy[i][j]
  #If the quantity of edges is equal to the quantity of edges in the combination, 
  # then the combination is a vertex cover
  return s == 0
     
def bruteForceVertexCover(vertex, matrix):
  #Count the quantity of edges on graph
  for r in range(1, len(vertex) + 1):
    #Create all possible combinations of vertex
    for c in itertools.combinations(vertex,r):
      c=list(c)
      if bruteForceVerification(c, vertex, matrix):
        return c
  return []

## -------------------------------------------------------------------------
# Main function
if __name__ == "__main__":
  ## Read data
  if len( sys.argv ) != 3:
    print( "Usage: python3", sys.argv[ 0 ], "<n> <p>" )
    print( "n: number of vertex" )
    print( "p: probability of edge" )
    sys.exit( 1 )
  # end if
  n = int( sys.argv[ 1 ] ) #Vertex
  p = float( sys.argv[ 2 ] ) #Edge probability


  #Create graph
  #vertex, matrix = createGraph(n,p)
  
  #Base example for testing
  vertex =[0,1,2,3,4,5,6]
  matrix=[
    [0,1,0,0,0,0,0],
    [1,0,1,0,0,0,0],
    [0,1,0,1,1,0,0],
    [0,0,1,0,1,1,1],
    [0,0,1,1,0,1,0],
    [0,0,0,1,1,0,0],
    [0,0,0,1,0,0,0]
    ]
  
  printGraph(vertex, matrix)
  C = aproxVertexCover(vertex, matrix)
  print("Approximated Vertex Cover: ", C)
  optimal = bruteForceVertexCover(vertex, matrix)
  print("Optimal Vertex Cover: ", optimal)

##eof - VertexCover.py