sequencia, qt_proc = input(), int(input())

while True:
    qt_ciclos = 0
    qt_leitura = 0
    for acao in sequencia:
        if acao == 'W' and qt_leitura > 0:
            qt_leitura = 0
            qt_ciclos += 2
        elif acao == 'W' and qt_leitura == 0:
            qt_ciclos += 1
        else:
            if qt_leitura < qt_proc:
                qt_leitura += 1
            else:
                qt_leitura = 1
                qt_ciclos += 1
    if qt_leitura > 0:
        qt_ciclos += 1

    print(qt_ciclos)

    try:
        sequencia, qt_proc = input(), int(input())
    except EOFError:
        break