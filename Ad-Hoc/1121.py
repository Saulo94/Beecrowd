direcoes = ['N', 'L', 'S', 'O']
qt_lin, qt_col, qt_inst = map(int, input().split())

while qt_lin or qt_col or qt_inst:
    posicao = None
    coordenada = None
    qt_figurinhas = 0
    mapa = [['' for i in range(qt_col)] for j in range(qt_lin)]

    for linha in range(qt_lin):
        for i, item in enumerate(input()):
            mapa[linha][i] = item
            if item == 'N' or item == 'S' or item == 'L' or item == 'O':
                posicao = direcoes.index(item)
                coordenada = (linha, i)
                mapa[linha][i] = '.'
    for movimento in input():
        if movimento == 'D':
            posicao = (posicao + 1) % 4
        elif movimento == 'E':
            posicao = (posicao - 1) % 4
        else:
            if posicao == 0 and coordenada[0] > 0: #Norte
                prox_casa = mapa[coordenada[0] - 1][coordenada[1]]
                if prox_casa == '*':
                    mapa[coordenada[0] - 1][coordenada[1]] = '.'
                    coordenada = (coordenada[0] - 1, coordenada[1])
                    qt_figurinhas += 1
                elif prox_casa == '.':
                    coordenada = (coordenada[0] - 1, coordenada[1])
            elif posicao == 1 and coordenada[1] < qt_col - 1: #Leste
                prox_casa = mapa[coordenada[0]][coordenada[1] + 1]
                if prox_casa == '*':
                    mapa[coordenada[0]][coordenada[1] + 1] = '.'
                    coordenada = (coordenada[0], coordenada[1] + 1)
                    qt_figurinhas += 1
                elif prox_casa == '.':
                    coordenada = (coordenada[0], coordenada[1] + 1)
            elif posicao == 2 and coordenada[0] < qt_lin - 1: #Sul
                prox_casa = mapa[coordenada[0] + 1][coordenada[1]]
                if prox_casa == '*':
                    mapa[coordenada[0] + 1][coordenada[1]] = '.'
                    coordenada = (coordenada[0] + 1, coordenada[1])
                    qt_figurinhas += 1
                elif prox_casa == '.':
                    coordenada = (coordenada[0] + 1, coordenada[1])
            elif posicao == 3 and coordenada[1] > 0: #Oeste
                prox_casa = mapa[coordenada[0]][coordenada[1] - 1]
                if prox_casa == '*':
                    mapa[coordenada[0]][coordenada[1] - 1] = '.'
                    coordenada = (coordenada[0], coordenada[1] - 1)
                    qt_figurinhas += 1
                elif prox_casa == '.':
                    coordenada = (coordenada[0], coordenada[1] - 1)
    print(qt_figurinhas)
    qt_lin, qt_col, qt_inst = map(int, input().split())
