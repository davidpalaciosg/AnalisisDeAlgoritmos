import random, sys
from MineSweeperBoard import *

## ========================================================================
if len( sys.argv ) < 4:
  print( "Usage: python3", sys.argv[ 0 ], "width height mines" )
  sys.exit( 1 )
# end if
w = int( sys.argv[ 1 ] )
h = int( sys.argv[ 2 ] )
m = int( sys.argv[ 3 ] )
board = MineSweeperBoard( w, h, m )
cont = 0

def isValid(x, y,N,M):
    # Returns true if valid
    return (x >= 0 and y >= 0 and x < N and y < M)

while not board.have_won( ) and not board.have_lose( ):
  #click = [board.height()][board.width()]
  
  if cont == 0:
    cont = cont + 1
    print( board )
    i = random.randint( 0, board.width( ) - 1 )
    auxi=i
    j = random.randint( 0, board.height( ) - 1 )
    auxj=j
    board.click( i, j )
    print(board.m_Mines[i][j])
  else:
    print( board )
    if(auxi == 0 and auxj == 0):
      if(board.m_Mines[i][j] == 0):
        auxi = auxi +1
        auxj = auxj +1
        board.click( auxi, auxj )
        print(board.m_Mines[auxi][auxj])
      else:
        probabilidad = board.m_Mines[auxi][auxj]/3
        if(probabilidad == 1):
          auxi = auxi +2
          auxj = auxj +2
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
        else:
          auxi = auxi +1
          auxj = auxj +2
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
    else:    
      ##auxi = auxi +1
      #auxj = auxj 
      #board.click( auxi, auxj )
      #print(board.m_Mines[auxi][auxj])
      
      if (auxi == board.width()-1 and auxj < board.height()-1):
          auxi = auxi
          auxj = auxj +1
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
      if(auxi == board.width()-1 and auxj == board.height()-1):
          auxi = auxi
          auxj = auxj -1 
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
      if (auxj == board.height()-1 and auxi < board.width()-1):
          auxi = auxi + 1
          auxj = auxj 
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
      if(auxj == board.height()-1 and auxi == board.width()-1):
          auxi = auxi 
          auxj = auxj -1 
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])
      if (auxi < board.width()-1 and auxj < board.height()-1 ):
          auxi = auxi +1
          auxj = auxj  
          board.click( auxi, auxj )
          print(board.m_Mines[auxi][auxj])  
    

# end while

print( board )
if board.have_won( ):
  print( "You won!" )
elif board.have_lose( ):
  print( "You lose :-(" )
# end if
