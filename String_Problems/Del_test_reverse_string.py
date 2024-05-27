# Funcion para resivir un string y regresarlo revertido

def rever_str(cadena_a_revertir):
    return cadena_a_revertir[::-1]

texto_prueba = "Hola esto es una prueba"
texto_revertido = rever_str(texto_prueba)
print(texto_revertido)

# Usando un ciclo para iterar en cada uno
def rever_str2(cadena_a_revertir2):
    str_revertido = ""

    for i in cadena_a_revertir2:
        str_revertido = i + str_revertido
    return str_revertido

print("------------")
texto_prueba2 = "Hola esto es una prueba"
texto_revertido2 = rever_str2(texto_prueba2)
print(texto_revertido2)


# Revertir por palabras

def invertir_palabras(cadena):
    # Convertir primero en una lista de palabras
    palabras = cadena.split()
    # Invertir el order de las palabras 
    palabras_invertidas = palabras[::-1]
    # Unir las palabras invertidas
    cadena_invertida = " ".join(palabras_invertidas)
    return cadena_invertida

print("--------------")
texto = "Hola este es un ejemplo con todas las palabras"
texto_inverso = invertir_palabras(texto)
print(texto_inverso)