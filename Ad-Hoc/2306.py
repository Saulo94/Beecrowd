from math import floor


def escada_perfeita(qt_colunas, colunas):
    inicial = ((2 * sum(colunas) / qt_colunas) - qt_colunas + 1) / 2

    if (inicial - floor(inicial) != 0) or (inicial < 1):
        return -1

    movimentos = 0
    for i in range(qt_colunas):
        if colunas[i] > inicial + i:
            movimentos += colunas[i] - inicial - i

    return int(movimentos)


print(escada_perfeita(int(input()), [int(i) for i in input().split()]))
