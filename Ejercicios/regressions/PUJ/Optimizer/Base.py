## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import numpy

class Base:

  '''
  '''
  m_Cost = None
  m_Alpha = 1e-2
  m_Epsilon = 1e-6
  m_NumberOfIterations = 1000
  m_RealIterations = 0
  m_NumberOfDebugIterations = 10

  '''
  '''
  def __init__( self, cost ):
    self.m_Cost = cost
  # end def

  def setLearningRate( self, a ):
    self.m_Alpha = a
  # end def

  def setLambda( self, l ):
    self.m_Lambda = l
  # end def

  def setEpsilon( self, e ):
    self.m_Epsilon = e
  # end def

  def setNumberOfIterations( self, i ):
    self.m_NumberOfIterations = i
  # end def

  def setNumberOfDebugIterations( self, i ):
    self.m_NumberOfDebugIterations = i
  # end def

  def setDebugFunction( self, f ):
    self.m_DebugFunction = f
  # end def

  def realIterations( self ):
    return self.m_RealIterations
  # end def

  def Fit( self ):
    pass
  # end def

## eof - $RCSfile$
