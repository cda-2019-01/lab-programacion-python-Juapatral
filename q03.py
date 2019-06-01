##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

import pandas as pd
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# split file
prueba=file.groupby(0).sum()[1]
prueba2 = []
for a in range(5):
    prueba2.append(list(prueba.index)[a] + "," + str(list(prueba)[a]))

print("\n".join(prueba2))