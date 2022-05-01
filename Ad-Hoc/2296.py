qt_trilhas = int(input())

desnivel_menor = (1e8 + 1, 0)
for i_trilha in range(1, qt_trilhas + 1):
    qt_pontos, *pontos = map(int, input().split())

    desnivel_atras = 0
    desnivel_frente = 0
    for i in range(qt_pontos - 1):
        dif = pontos[i + 1] - pontos[i]
        if dif > 0:
            desnivel_frente += dif
    for i in range(qt_pontos - 1, 0, -1):
        dif = pontos[i - 1] - pontos[i]
        if dif > 0:
            desnivel_atras += dif
    desnivel = min(desnivel_frente, desnivel_atras)
    if desnivel < desnivel_menor[0]:
        desnivel_menor = (desnivel, i_trilha)

print(desnivel_menor[1])
