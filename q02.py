##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

import pandas as pd
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# split file
prueba=file.groupby(0).count()[2]
prueba2 = []
for a in range(5):
    prueba2.append(list(prueba.index)[a] + "," + str(list(prueba)[a]))

print("\n".join(prueba2))

