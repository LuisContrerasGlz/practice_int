tamaño = 5

for i in range(tamaño-1, -1,-1):
    print("*" * (2 * i +1))

def pyramid(tamaño_p):
    for i in range(tamaño-1, -1,-1):
        print("*" * (2 * i +1))

pyramid(5)
pyramid(7)
pyramid(10)
