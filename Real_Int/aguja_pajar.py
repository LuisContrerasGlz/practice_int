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