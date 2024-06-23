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
