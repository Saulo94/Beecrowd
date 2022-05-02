lista_final = []
while True:
    try:
        qut_moeda = int(input().split()[0])
    except EOFError:
        break

    lista_moeda = []

    for i in range(qut_moeda):
        lista_moeda.append(int(input()))
    salto = int(input())

    soma, i = 0, len(lista_moeda) - 1
    while i >= 0:
        soma += lista_moeda[i]
        i -= salto

    qut_div = 0
    i = 2
    while i <= soma / 2:
        if soma % i == 0:
            qut_div += 1
        i += 1

    if qut_div == 0 and soma != 1:
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I’ll hit you.")
