def ponto_esta_no_retangulo(ponto, ret):
    return ret[0][0] <= ponto[0] <= ret[3][0] and ret[0][1] <= ponto[1] <= ret[1][1]


def reta_intersecta_circulo(ponto, r, pontos):
    if pontos[0][0] == pontos[1][0]:
        if pontos[0][1] < ponto[1]:
            return ((ponto[0] - pontos[0][0]) ** 2 + (ponto[1] - pontos[0][1]) ** 2) ** (1 / 2) <= r
        elif ponto[1] < pontos[1][1]:
            return ((ponto[0] - pontos[1][0]) ** 2 + (ponto[1] - pontos[1][1]) ** 2) ** (1 / 2) <= r
        else:
            return abs(ponto[0] - pontos[0][0]) <= r
    else:
        if pontos[0][0] < ponto[0]:
            return ((ponto[0] - pontos[0][0]) ** 2 + (ponto[1] - pontos[0][1]) ** 2) ** (1 / 2) <= r
        elif ponto[0] < pontos[1][0]:
            return ((ponto[0] - pontos[1][0]) ** 2 + (ponto[1] - pontos[1][1]) ** 2) ** (1 / 2) <= r
        else:
            return abs(ponto[1] - pontos[1][1]) <= r


def interseccao(circ, ret):
    ponto_circ = circ[0]
    r = circ[1]

    return (ponto_esta_no_retangulo(ponto_circ, ret) or
            reta_intersecta_circulo(ponto_circ, r, (ret[1], ret[0])) or
            reta_intersecta_circulo(ponto_circ, r, (ret[2], ret[1])) or
            reta_intersecta_circulo(ponto_circ, r, (ret[2], ret[3])) or
            reta_intersecta_circulo(ponto_circ, r, (ret[3], ret[0])))


magias = {'fire': (200, 20, 30, 50),
          'water': (300, 10, 25, 40),
          'earth': (400, 25, 55, 70),
          'air': (100, 18, 38, 60)}
qt_casos = int(input())

for _ in range(qt_casos):
    w, h, x0, y0 = map(int, input().split())
    magia, nivel, cx, cy = input().split()
    nivel = int(nivel)
    retangulo = ((x0, y0), (x0, y0 + h), (x0 + w, y0 + h), (x0 + w, y0))
    circulo = (int(cx), int(cy))
    dano, raio = magias[magia][0], magias[magia][nivel]

    if interseccao((circulo, raio), retangulo):
        print(dano)
    else:
        print(0)

