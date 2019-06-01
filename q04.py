##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

import pandas as pd
# read file
file = pd.read_csv('data.csv',sep='\t',header=None)

# creates month column
file['date'] = file[2].str.split('-')
file['month'] = [f[1] for f in file['date']]

# group by months

# split file
prueba=file.groupby('month').count()[0]
prueba2 = []
for a,x in enumerate(prueba.index):
    prueba2.append(list(prueba.index)[a] + "," + str(list(prueba)[a]))

print("\n".join(prueba2))