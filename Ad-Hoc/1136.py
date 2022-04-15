qt_numeros, qt_bolas = map(int, input().split())

while qt_numeros or qt_bolas:
    numeros_na_ordem = set()
    numeros = set()
    for bola in map(int, input().split()):
        numeros.add(bola)
        for numero in numeros:
            dif = abs(numero - bola)
            if dif <= qt_numeros:
                numeros_na_ordem.add(dif)
    if len(numeros_na_ordem) == qt_numeros + 1:
        print('Y')
    else:
        print('N')

    qt_numeros, qt_bolas = map(int, input().split())
