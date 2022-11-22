## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import numpy
from .Base import *


class GradientDescent( Base ):

  '''
  '''
  def __init__( self, cost ):
    super( ).__init__( cost )
  # end def

  def Fit( self ):
    [ J0, g ] = self.m_Cost.evaluate( True )
    stop = False
    self.m_RealIterations = 0
    while not stop:
      self.m_Cost.updateModel( -self.m_Alpha * g ) #Learning rate es el alpha
      [ J1, g ] = self.m_Cost.evaluate( True )
      stop = stop or self.m_RealIterations >= self.m_NumberOfIterations
      self.m_RealIterations += 1
      J0 = J1
    # end while
  # end def

## eof - $RCSfile$
