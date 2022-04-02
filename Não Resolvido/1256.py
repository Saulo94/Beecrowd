qt_teste = int(input())

for i in range(qt_teste):
    espaco, qt_numeros = map(int, input().split())

    lista_numeros = [[] for _ in range(espaco)]

    for numero in map(int, input().split()):
        lista_numeros[numero % espaco].append(numero)

    for index, numeros in enumerate(lista_numeros):
        print(" -> ".join([str(index)] + list(map(str, lista_numeros[index])) + ["\\"]))

    if i == qt_teste - 1:
        break
    else:
        print("")