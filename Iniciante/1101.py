numero1, numero2 = map(int, input().split())

while numero1 > 0 and numero2 > 0:
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    print("{0} Sum={1}".format(
        " ".join([str(num) for num in range(numero1, numero2 + 1)]),
        int(((numero2 - numero1 + 1) / 2) * (numero1 + numero2))))
    numero1, numero2 = map(int, input().split())