##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

import pandas as pd

# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# create columns
file['largo3'] = [len(a) for a in file[3].str.split(',')]
file['largo4'] = [len(a) for a in file[4].str.split(',')]
file2 = file[[0,'largo3','largo4']]

for i in range(len(file2)):
    print(file2[0][i] + ',' + 
    str(file2['largo3'][i]) + ',' + 
    str(file2['largo4'][i])
    )