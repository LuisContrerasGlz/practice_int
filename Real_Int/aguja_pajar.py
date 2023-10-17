"""

Encontrar la aguja en el pajar. 

Es un arreglo de palabras revueltas y en alguna posicion está la palabra "aguja", tienes que encontrar la palabra e imprimir su posición.

"""

def aguja(palabra,arreglo):
    if palabra in arreglo:
        pos = arreglo.index(palabra)
    else:
        print("Palabra no encontrada")
        pos = -1
    return pos 


arreglo=['hola','adios','bye','hello','aguja','otro','some']
palabra='aguja'
print(aguja(palabra,arreglo))

"""

The time complexity (big O notation) of the given code is O(n), where 'n' is the length of the input array arreglo.

The primary operation affecting the time complexity is the arreglo.index(palabra) function, 
which searches for the index of the palabra in the array. 

In the worst case, this function may have to scan through the entire array to find the index of the given word. 
Therefore, the time complexity is linear with respect to the size of the array.

"""