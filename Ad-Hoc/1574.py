qt_teste = int(input())
for _ in range(qt_teste):
    qt_instrucao = int(input())
    lista_instrucao = []
    p = 0
    for __ in range(qt_instrucao):
        lista_instrucao.append(input())
        if lista_instrucao[-1][:4] == "SAME":
            lista_instrucao[-1] = lista_instrucao[int(lista_instrucao[-1][7:]) - 1]
        if lista_instrucao[-1] == "RIGHT":
            p += 1
        else:
            p -= 1
    print(p)
