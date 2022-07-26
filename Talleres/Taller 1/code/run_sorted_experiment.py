## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## @author David Enrique Palacios-Garcia (david_palacios@javeriana.edu.co)
## @author Karen Sofia Coral Godoy (corallg ksofia@javeriana.edu.co) 
## =========================================================================
"""
Manual de uso:
Ejecutar en consola:

python run_sorted_experiment.py tamMinimo tamMaximo salto 
"""
from random import randint
import struct, sys, time
from NaiveBubbleSort import *
from ImprovedBubbleSort import *
from InsertionSort import *

## -------------------------------------------------------------------------
def IsSorted( S ):
  f = True
  for i in range( len( S ) - 1 ):
    f = f and not( S[ i + 1 ] < S[ i ] )
  # end for
  return f
# end def

## -------------------------------------------------------------------------
def DoExperiment( S, f ):
  r = 10
  t = 0
  s = True
  for i in range( r ):
    C = S.copy( )
    start = time.time( )
    f( C )
    end = time.time( )
    s = s and IsSorted( C )
    t += float( end - start )
  # end for
  return [ s, t / float( r ) ]
# end def

## -------------------------------------------------------------------------
def GenerateRandomNumber():
  return randint(-1000000,1000000)
## -------------------------------------------------------------------------
# Inputs
b = int( sys.argv[ 1 ] )
e = int( sys.argv[ 2 ] )
s = int( sys.argv[ 3 ] )

# Generate random sequence
input_sequence = []
for i in range( e ):
  input_sequence.append(GenerateRandomNumber())
# end for

input_sequence.sort() # Sort the sequence with python sort

# Perform experiments
for n in range( b, e + 1, s ):
  nbr = DoExperiment( input_sequence[ 0 : n ], NaiveBubbleSort )
  ibr = DoExperiment( input_sequence[ 0 : n ], ImprovedBubbleSort )
  inr = DoExperiment( input_sequence[ 0 : n ], InsertionSort )
  if not( nbr[ 0 ] and ibr[ 0 ] and inr[ 0 ] ):
    print( "ERROR: Input sequence was not ordered" )
    sys.exit( 1 )
  # end if
  print( n, nbr[ 1 ], ibr[ 1 ], inr[ 1 ] )
# end for

## eof - run_experiment.py
