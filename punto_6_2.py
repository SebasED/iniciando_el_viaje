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

# Solution with slicing
# Wrong array
array = [[2,4,3,6],[8,3,4,5],[7,1,3,10],[9,2,1,4]]
print(array)

# Fix the array by modifying each row with spacing  
array[0] = array[0][0:-1] + [sum(array[0][0:-1])]
array[1] = array[1][0:-1] + [sum(array[1][0:-1])]
array[2] = array[2][0:-1] + [sum(array[2][0:-1])]
array[3] = array[3][0:-1] + [sum(array[3][0:-1])]

# Print correct array in the console
print(array) 