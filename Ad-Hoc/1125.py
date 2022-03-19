g, p = (int(i) for i in input().split())

while g != 0 and p != 0:
    colocacoes = {}
    entrada = input().split()
    for i in range(p):
        colocacoes[i + 1] = [int(entrada[i])]

    for _ in range(g - 1):
        entrada = input().split()
        for i in range(p):
            colocacoes[i + 1].append(int(entrada[i]))

    qt_pontuacao = int(input())

    for _ in range(qt_pontuacao):
        sistema_pontuacao = {}
        pontuacao = {}
        entrada = input().split()
        for i in range(1, int(entrada[0]) + 1):
            sistema_pontuacao[i] = int(entrada[i])

        maior_pontuacao = 0
        maiores_pilotos = []
        for key in colocacoes.keys():
            pontos = 0
            for item in colocacoes[key]:
                try:
                    pontos += sistema_pontuacao[item]
                finally:
                    continue
            pontuacao[key] = pontos
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                maiores_pilotos = [key]
            elif pontos == maior_pontuacao:
                maiores_pilotos.append(key)
        print(*maiores_pilotos)

    g, p = (int(i) for i in input().split())


