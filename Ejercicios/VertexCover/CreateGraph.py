## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
import random, sys

def createGraph(n,p):
  
  #Create list of vertex
  vertex = []
  #Create edges matrix
  matrix = [ [ 0 for i in range( n ) ] for j in range( n ) ]
  for i in range( n ):
    vertex.append( i )
    for j in range( n ):
      if i != j:
        q = random.uniform( 0, 1 )
        if q < p:
          value = random.randint( 1, 100 )
          matrix[ i ][ j ] = value
          matrix[ j ][ i ] = value
        # end if
      # end if
    # end for
  # end for
  #Return graph
  return (vertex, matrix)
## end def

#Print a graph
def printGraph(vertex, matrix):
  print("Vertex: ", vertex)
  print("Matrix: ")
  for i in range(0,len(vertex)):
    for j in range(0,len(vertex)):
      print(matrix[i][j], end=" ")
    print()
## end def  

#Verify if the matrix is empty
def isMatrixEmpty(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if matrix[i][j] > 0:
        return False
  return True

## eof - CreateGraph.py
