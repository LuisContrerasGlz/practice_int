# Build an inverted pyramid base on input to see how big

tamaño = 5
for i in range(tamaño-1, -1,-1):
    print(" " * (tamaño - i - 1) + "*" * (2 * i +1))

# Funtion
    
def inverted_pyramid(tamaño_p):
    for i in range(tamaño_p-1, -1,-1):
        print(" " * (tamaño_p - i - 1) + "*" * (2 * i +1) )

inverted_pyramid(5)
inverted_pyramid(7)
inverted_pyramid(10)