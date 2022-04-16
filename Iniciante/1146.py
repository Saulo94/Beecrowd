numero = int(input())

while numero:
    for num in range(1, numero):
        print("{0}".format(num), end=" ")
    print(numero)

    numero = int(input())
