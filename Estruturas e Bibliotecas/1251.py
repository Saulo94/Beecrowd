def quick_sort(elementos):
    menores = []
    iguais = []
    maiores = []
    pivo = elementos[0]
    for elemento in elementos:
        if elemento[1] > pivo[1]:
            maiores.append(elemento)
        elif elemento[1] < pivo[1]:
            menores.append(elemento)
        else:
            iguais = inserir_frequencia_igual(iguais, elemento)
    if menores and maiores:
        return quick_sort(menores) + iguais + quick_sort(maiores)
    elif not menores and maiores:
        return iguais + quick_sort(maiores)
    elif menores and not maiores:
        return quick_sort(menores) + iguais
    else:
        return iguais


def inserir_frequencia_igual(lista, elemento):
    if len(lista) == 0:
        return [elemento]
    metade = len(lista) // 2
    if lista[metade][0] < elemento[0]:
        return inserir_frequencia_igual(lista[:metade], elemento) + lista[metade:]
    if lista[metade][0] > elemento[0]:
        return lista[:metade + 1] + inserir_frequencia_igual(lista[metade + 1:], elemento)


def ordernar_frequencias(dicionario):
    lista = []
    for codigo in dicionario:
        lista.append([codigo, dicionario[codigo]])
    return quick_sort(lista)


palavra = input()
while True:
    frequencia = {}
    for letra in palavra:
        codigo = ord(letra)
        if frequencia.get(codigo):
            frequencia[codigo] += 1
        else:
            frequencia[codigo] = 1

    for item in ordernar_frequencias(frequencia):
        print(*item)

    try:
        palavra = input()
        print("")
    except EOFError:
        break
