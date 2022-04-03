while True:
    numeros = []
    while len(numeros) != 2:
        num = float(input())
        if 0 <= num <= 10:
            numeros.append(num)
        else:
            print("nota invalida")

    print("media = {0:.2f}".format((numeros[0] + numeros[1]) / 2))

    res = 0
    while res != 1 and res != 2:
        print("novo calculo (1-sim 2-nao)")
        res = int(input())
    if res == 2:
        break
