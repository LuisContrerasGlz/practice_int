# En otro me pidieron que de un arreglo de Strings, eliminara todas las palabras repetidas e imprimiera el resultado. 

def elimina_repetidos(arreglo):
    palabras_unicas = []
    for palabra in arreglo:
        if palabra not in palabras_unicas:
           palabras_unicas.append(palabra)
    return palabras_unicas 
        

# Arreglo de strings con palabras repetidas
arreglo = ["Hola", "Mundo", "Hola", "Python", "Mundo", "Programación"]

print(elimina_repetidos(arreglo))


"""

The time complexity of the provided code is O(n^2), where 'n' is the length of the input array arreglo.

Here's the breakdown:

The code uses a for loop to iterate over each element in the input array arreglo. This loop contributes O(n) time complexity.

Inside the loop, it uses the if palabra not in palabras_unicas condition to check whether the current element is already in the palabras_unicas list. Checking whether an element is in a list has a time complexity of O(n) for each element. Since this check is performed within the loop, the worst-case time complexity is O(n) for the check.

If the current element is not in palabras_unicas, it appends the element to the palabras_unicas list. The append operation typically runs in constant time, O(1), but since it's executed within the loop, it contributes O(n) to the overall time complexity.

As a result, the total time complexity is O(n) for the outer loop multiplied by O(n) for the inner loop, which results in O(n^2). This quadratic time complexity makes the code less efficient, especially for large input arrays. 

"""

# Sorted


def remove_duplicates2(string):
    return "".join(sorted(set(string), key=string.index))


print(remove_duplicates2("hello world dude"))