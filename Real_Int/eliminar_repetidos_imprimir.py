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