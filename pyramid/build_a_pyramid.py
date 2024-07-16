# Build a pyramid base on input to see how big

tamaño = 5
for i in range(0,tamaño,1):
    print(" " * (tamaño - i - 1) + "*" * (2 * i +1) )