def mostrar_tabuleiro(matriz, alt, lar):
    for i in range(alt):
        # linha a ser printada
        linha = ""
        for k in range(lar):
            # Verifica se a posição contém um pão de queijo
            if matriz[i][k] == '1':
                linha += '9'
                continue
            qt_paoqueijo = 0
            if i > 0 and matriz[i - 1][k] == '1':
                qt_paoqueijo += 1
            if i < alt - 1 and matriz[i + 1][k] == '1':
                qt_paoqueijo += 1
            if k > 0 and matriz[i][k - 1] == '1':
                qt_paoqueijo += 1
            if k < lar - 1 and matriz[i][k + 1] == '1':
                qt_paoqueijo += 1
            linha += str(qt_paoqueijo)
        print(linha)


qt_linhas, qt_colunas = map(int, input().split())

while True:
    mapa_paoqueijo = []
    for _ in range(qt_linhas):
        mapa_paoqueijo.append(input().split())

    mostrar_tabuleiro(mapa_paoqueijo, qt_linhas, qt_colunas)

    try:
        qt_linhas, qt_colunas = map(int, input().split())
    except EOFError:
        break
