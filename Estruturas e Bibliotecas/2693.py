def comparacao(termo1, termo2):
    for i, string in ((2, False), (1, True), (0, True)):
        if string:
            menor_len = min([len(termo1[i]), len(termo2[i])])
            for k in range(menor_len):
                if termo1[i][k] > termo2[i][k]:
                    return 2
                elif termo1[i][k] < termo2[i][k]:
                    return 1
        else:
            if termo1[i] < termo2[i]:
                return 1
            elif termo1[i] > termo2[i]:
                return 2


def merge_sort(sequencia):
    tam = len(sequencia)
    if tam == 1:
        return sequencia
    meio = tam // 2
    parte1 = merge_sort(sequencia[:meio])
    parte2 = merge_sort(sequencia[meio:])
    final = []
    i, j = 0, 0
    while True:
        if i < len(parte1) and j < len(parte2):
            if comparacao(parte1[i], parte2[j]) == 1:
                final.append(parte1[i])
                i += 1
            else:
                final.append(parte2[j])
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
    lista_alunos = []
    for _ in range(qt_alunos):
        nome, regiao, dist = input().split()
        lista_alunos.append((nome, regiao, int(dist)))
    for aluno in merge_sort(lista_alunos):
        print(aluno[0])
    try:
        qt_alunos = int(input())
    except EOFError:
        break
