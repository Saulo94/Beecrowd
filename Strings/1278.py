qt_linhas = int(input())

while qt_linhas:
    lista_linhas = []
    tam_max = 0
    for i in range(qt_linhas):
        lista_linhas.append([])
        tam = 0
        for palavra in input().split():
            tam += len(palavra)
            lista_linhas[i].append(palavra)
        if tam + len(lista_linhas[i]) - 1 > tam_max:
            tam_max = tam + len(lista_linhas[i]) - 1

    for i in range(qt_linhas):
        linha = " ".join(lista_linhas[i])
        print(" " * (tam_max - len(linha)) + linha)

    qt_linhas = int(input())
    if qt_linhas:
        print("")
