##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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

# creates max and mins

maxim = prueba3.groupby('dic').max()['value']
minim = prueba3.groupby('dic').min()['value']

prueba4 = []
for a,x in enumerate(maxim):
    prueba4.append(list(maxim.index)[a] + "," 
    + str(list(minim)[a]) + ',' 
    + str(list(maxim)[a])
    )

print("\n".join(prueba4))