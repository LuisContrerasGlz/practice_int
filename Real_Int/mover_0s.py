# Write a function to move all [0,1,5,4,32,80,0,4,0,1] 0 from to left and another to right

def cero_to_the_right(array):
    # Crea una nueva lista para almacenar los elementos reorganizados
    ceroTR = []

    # Agrega los elementos diferentes de cero a la nueva lista
    for element in array:
        if element != 0:
            ceroTR.append(element)

    # Calcula la cantidad de ceros ignorados
    num_zeros_ignored = len(array) - len(ceroTR)

    # Agrega los ceros faltantes al final de la nueva lista
    for i in range(num_zeros_ignored):
        ceroTR.append(0)

    # Retorna la lista modificada
    return ceroTR

def cero_to_the_left(array):
    # Crea una nueva lista para almacenar los elementos reorganizados
    ceroTL = []

    # Crea una lista sin los ceros, manteniendo el orden original
    for element in array:
        if element != 0:
            ceroTL.append(element)

    # Calcula la cantidad de ceros ignorados
    num_zeros_ignored = len(array) - len(ceroTL)

    # Agrega los ceros al principio de la nueva lista
    for i in range(num_zeros_ignored):
        ceroTL.insert(0, 0)

    # Retorna la lista modificada
    return ceroTL



array = [0,1,5,4,32,80,0,4,0,1]
print(array)
print(cero_to_the_right(array))
print(cero_to_the_left(array))


"""

The time complexity of the provided code is O(n), where 'n' is the length of the input array array.

Here's the breakdown:

The first for loop iterates through the elements in the input array array, which takes O(n) time.

The second for loop iterates a number of times equal to num_zeros_ignored. The value of num_zeros_ignored is determined by subtracting the length of ceroTR from the length of the original array, which is still O(n).

All other operations in the code run in constant time (O(1)).

Therefore, the overall time complexity is O(n) because the dominant factor in the code's execution time is the iteration over the elements in the input array.


"""