"""
La siguiente matriz (o lista con listas anidadas) debe cumplir que el cuarto elemento 
de cada fila se la suma de los tres primeros elementos de la fila respectiva. Si nota 
las sumas que se encuentran están erróneas, debe modificarlas dando 2 soluciones, 
una con append y otra con slicing.

Ayuda: la función sum(lista) devuelve la suma de todos los elementos de la lista.

Matriz errónea: 
matriz = [ 
    [2, 4, 3, 6], 
    [8, 3, 4, 5], 
    [7, 1, 3, 10], 
    [9, 2, 1, 4] 
] 
 
Debes llegar a: 
matriz = [ 
    [2, 4, 3, 9], 
    [8, 3, 4, 15], 
    [7, 1, 3, 11], 
    [9, 2, 1, 12] 
]
"""

# Solution with append method
# Wrong array
array = [[2,4,3,6],[8,3,4,5],[7,1,3,10],[9,2,1,4]]
print(array)

# Separate the array in rows without the last element from each row
row_1 = array[0][0:-1]
row_2 = array[1][0:-1]
row_3 = array[2][0:-1]
row_4 = array[3][0:-1]

# Add to each row an element, that element is the sum of the same row
row_1.append(sum(row_1))
row_2.append(sum(row_2))
row_3.append(sum(row_3))
row_4.append(sum(row_4))

# Delete all elements of the array
array = []

# Build the array with the correct values in each row 
array.append(row_1)
array.append(row_2)
array.append(row_3)
array.append(row_4)

# Print correct array in the console
print(array)