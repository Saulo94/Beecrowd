qt_part, qt_rod = map(int, input().split())

i_teste = 0
while qt_part:
    i_teste += 1
    participantes = list(map(int, input().split()))
    for i in range(qt_rod):
        _, ordem, *lista = map(int, input().split())
        k = 0
        while k < len(lista):
            if lista[k] != ordem:
                del(participantes[k])
                del(lista[k])
            else:
                k += 1

    print("Teste {0}\n{1}\n".format(i_teste, participantes[0]))

    qt_part, qt_rod = map(int, input().split())
