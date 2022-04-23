linhas, colunas = map(int, input().split())
matriz = [input().split() for _ in range(linhas)]

parar = False
coordenadas = 0, 0
for i in range(1, linhas - 1):
    for j in range(1, colunas - 1):
        if matriz[i][j] == '42':
            if ('7' == matriz[i - 1][j]
                    == matriz[i - 1][j + 1]
                    == matriz[i][j + 1]
                    == matriz[i + 1][j + 1]
                    == matriz[i + 1][j]
                    == matriz[i + 1][j - 1]
                    == matriz[i][j - 1]
                    == matriz[i - 1][j - 1]):
                coordenadas = i + 1, j + 1
                parar = True
        if parar:
            break
    if parar:
        break

print(*coordenadas)
