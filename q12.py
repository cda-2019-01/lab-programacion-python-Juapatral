##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

import pandas as pd
from itertools import chain
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# create needed data
file['data'] = file[3].str.split(',')

file2 = file[3].str.split(',',expand=True)
file2['number'] = file[1]

lista = []

for a in range(4):
    lista += (list(file2[a]))

file3 = pd.DataFrame(data={'letra':lista, 'numero':(list(file2['number'])*4)})

prueba = file3.groupby('letra').sum()

prueba2 = []
for a,x in enumerate(list(prueba.index)):
    prueba2.append(list(prueba.index)[a] + "," + str(list(prueba['numero'])[a]))

print("\n".join(prueba2))

