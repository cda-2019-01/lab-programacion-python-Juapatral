##
## Imprima la suma de la segunda columna.
##

# read file
file = open("data.csv",'r').readlines()

# split file
file = [a[:-1].split('\t') for a in file]

# sum
print(sum([int(row[1]) for row in file]))
