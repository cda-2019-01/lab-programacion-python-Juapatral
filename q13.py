##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

import pandas as pd
from itertools import chain
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# create needed data
file['data'] = file[4].str.split(',')
prueba = [[b.split(',') for b in a] for a in list(file['data'])]
prueba2 = list(chain(*list(chain(*prueba))))
prueba3 = [list(chain(*a)) for a in prueba]
prueba4 = [sum([int(b[4:]) for b in a]) for a in prueba3]

for a in range(len(list(file[0]))):
    print(file[0][a],prueba4[a],sep=',')
