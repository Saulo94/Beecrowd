numeros = []
qt_grito = 0
while qt_grito < 3:
    numero = 0
    entrada = input()
    while entrada != "caw caw":
        for i, olho in enumerate(entrada[::-1]):
            if olho == '*':
                numero += 2 ** i
        entrada = input()
    qt_grito += 1
    numeros.append(numero)

for numero in numeros:
    print(numero)
