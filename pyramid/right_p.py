tamaño = 5

for i in range(tamaño):
    print("*" * (2 * i +1) )

def pyramid(tamaño_p):
    for i in range(tamaño_p):
        print("*" * (2 * i +1))

pyramid(5)
pyramid(7)
pyramid(10)