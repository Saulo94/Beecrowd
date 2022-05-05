def comparacao(termo1, termo2):
    for i, mod in ((1, False), (2, True), (3, True), (0, None)):
        if mod is None:
            menor_len = min([len(termo1[i]), len(termo2[i])])
            for k in range(menor_len):
                if termo1[i][k] > termo2[i][k]:
                    return 2
                else:
                    return 1
        if mod:
            if termo1[i] < termo2[i]:
                return 1
            elif termo1[i] > termo2[i]:
                return 2
        else:
            if termo1[i] > termo2[i]:
                return 1
            elif termo1[i] < termo2[i]:
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


quat_teste = int(input())
for i_teste in range(1, quat_teste + 1):
    renas_total, renas_treno = map(int, input().split())
    lista_rena = []
    for _ in range(renas_total):
        nome, peso, idade, altura = input().split()
        lista_rena.append((nome, int(peso), int(idade), float(altura)))
    print("CENARIO {" + str(i_teste) + "}")
    for i, rena in enumerate(merge_sort(lista_rena)[:renas_treno]):
        print(i + 1, "-", rena[0])
