# Build a pyramid base on input to see how big

tamaño = 5
for i in range(0,tamaño,1):
    print(" " * (tamaño - i - 1) + "*" * (2 * i +1) )

# Funtion
    
def pyramid(tamaño_p):
    for i in range(tamaño_p):
        print(" " * (tamaño_p - i - 1) + "*" * (2 * i +1) )

pyramid(5)
pyramid(7)
pyramid(10)
