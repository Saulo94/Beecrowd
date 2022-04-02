def ordenar_pedidos(lista):
    tam = len(lista)
    if tam == 1:
        return lista
    meio = tam // 2
    parte1 = ordenar_pedidos(lista[:meio])
    parte2 = ordenar_pedidos(lista[meio:])
    final = []
    i, j = 0, 0
    while True:
        if i < len(parte1) and j < len(parte2):
            if parte1[i][0] < parte2[j][0]:
                final.append(parte1[i])
                i += 1
            elif parte1[i][0] > parte2[j][0]:
                final.append(parte2[j])
                j += 1
            else:
                if parte1[i][1] < parte2[j][1]:
                    final.append(parte2[j])
                    j += 1
                elif parte1[i][1] > parte2[j][1]:
                    final.append(parte1[i])
                    i += 1
                else:
                    if parte1[i][2] < parte2[j][2]:
                        final.append(parte1[i])
                        i += 1
                    elif parte1[i][2] > parte2[j][2]:
                        final.append(parte2[j])
                        j += 1
                    else:
                        final.append(parte1[i])
                        final.append(parte2[j])
                        i += 1
                        j += 1
        elif i < len(parte1) and j == len(parte2):
            final.append(parte1[i])
            i += 1
        elif i == len(parte1) and j < len(parte2):
            final.append(parte2[j])
            j += 1
        else:
            break
    return final


qt_alunos = int(input())
while True:
    lista_pedidos = []
    for aluno in range(qt_alunos):
        nome = input()
        cor, tam = input().split()
        lista_pedidos.append([cor, tam, nome])
    qt_alunos = int(input())
    if qt_alunos:
        print("\n".join("{0} {1} {2}".format(pedido[0], pedido[1], pedido[2])
                        for pedido in ordenar_pedidos(lista_pedidos)) + "\n")
    else:
        print("\n".join("{0} {1} {2}".format(pedido[0], pedido[1], pedido[2])
                        for pedido in ordenar_pedidos(lista_pedidos)))
        break
