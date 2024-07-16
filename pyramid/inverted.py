# Build an inverted pyramid base on input to see how big

tamaño = 5
for i in range(tamaño-1, -1,-1):
    print(" " * (tamaño - i - 1) + "*" * (2 * i +1))