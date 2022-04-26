alt, lar = map(int, input().split())
coord_1, coord_2 = (), ()

while True:
    for i in range(alt):
        for k, posicao in enumerate(input().split()):
            if posicao == '1':
                coord_1 = (i, k)
            elif posicao == '2':
                coord_2 = (i, k)

    tempo_min = abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])
    print(tempo_min)

    try:
        alt, lar = map(int, input().split())
    except EOFError:
        break
