dic_posicao = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
lista_movimentos = {(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)}

teste = 1
entrada = input()
while entrada != '0':
    pos_cavalo = int(entrada[0]), dic_posicao[entrada[1]]
    pos_peoes = set()
    qt_movimentos = 0

    for _ in range(8):
        entrada = input()
        pos_peoes.add((int(entrada[0]), dic_posicao[entrada[1]]))

    for movimento in lista_movimentos:
        nova_pos = pos_cavalo[0] + movimento[0], pos_cavalo[1] + movimento[1]
        if not (0 < nova_pos[0] < 9 and 0 < nova_pos[1] < 9):
            continue
        ataq_direita = nova_pos[0] + 1, nova_pos[1] + 1
        ataq_esquerda = nova_pos[0] + 1, nova_pos[1] - 1

        if (0 < ataq_direita[0] < 9 and 0 < ataq_direita[1] < 9) and \
                (0 < ataq_esquerda[0] < 9 and 0 < ataq_esquerda[1] < 9):
            if ataq_direita not in pos_peoes and ataq_esquerda not in pos_peoes:
                qt_movimentos += 1
        elif (0 < ataq_direita[0] < 9 and 0 < ataq_direita[1] < 9) and \
                not (0 < ataq_esquerda[0] < 9 and 0 < ataq_esquerda[1] < 9):
            if ataq_direita not in pos_peoes:
                qt_movimentos += 1
        elif not (0 < ataq_direita[0] < 9 and 0 < ataq_direita[1] < 9) and \
                (0 < ataq_esquerda[0] < 9 and 0 < ataq_esquerda[1] < 9):
            if ataq_esquerda not in pos_peoes:
                qt_movimentos += 1
        else:
            qt_movimentos += 1

    print("Caso de Teste #{0}: {1} movimento(s).".format(teste, qt_movimentos))

    teste += 1
    entrada = input()
