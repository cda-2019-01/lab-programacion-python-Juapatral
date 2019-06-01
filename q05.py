##
## Imprima el valor maximo y minimo por cada letra de 
## la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##


import pandas as pd
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

maxim = file.groupby(0).max()[1]
minim = file.groupby(0).min()[1]

prueba2 = []
for a,x in enumerate(maxim):
    prueba2.append(list(maxim.index)[a] + "," 
    + str(list(maxim)[a]) + ',' 
    + str(list(minim)[a])
    )

print("\n".join(prueba2))
