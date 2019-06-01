##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##

import pandas as pd
from itertools import chain
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# create needed data
file['data'] = file[4].str.split(',')
prueba = [[b.split(',') for b in a] for a in list(file['data'])]
prueba2 = list(chain(*list(chain(*prueba))))

# creates dataframe with needed data
prueba3 = pd.DataFrame([a.split(':') for a in prueba2], columns = ['dic','value'])

# split file
prueba4 = prueba3.groupby('dic').count()['value']
prueba2 = []
for a in range(len(prueba4)):
    prueba2.append(str(list(prueba4.index)[a]) + "," + str(list(prueba4)[a]))

print("\n".join(prueba2))