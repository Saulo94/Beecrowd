altura, comprimento = map(int, input().split())

while altura != 0 and comprimento != 0:
    qt_varreduras = 0
    alt_anterior = None
    for i, alt in enumerate(int(alt) for alt in input().split()):
        if i != 0:
            if alt > alt_anterior:
                qt_varreduras += alt - alt_anterior
            alt_anterior = alt
        else:
            alt_anterior = alt
        if i == comprimento - 1:
            qt_varreduras += altura - alt
    print(qt_varreduras)

    altura, comprimento = map(int, input().split())