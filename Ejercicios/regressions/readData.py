import pandas as pd
import numpy, sys
import PUJ

#df= pd.read_csv('data.csv')
#D= numpy.matrix(df)
D= numpy.matrix(numpy.loadtxt(sys.argv[1], delimiter= ','))

model= PUJ.Model.Linear(D)

print (model)
#print (model.evaluate([4]))