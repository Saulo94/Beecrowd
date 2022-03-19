def subtrair(el1, el2, el3):
    """recebe uma lista e um número e retorna essa mesma lista
    com seus elementos subtraídos pelo número
    list, int -> list"""
    minimo = min(dic[el1], dic[el2], dic[el3])
    dic[el1] -= minimo
    dic[el2] -= minimo
    dic[el3] -= minimo
    return minimo


dic = {"uc": 0, "dc": 0, "tc": 0,
       "ut": 0, "dt": 0, "tt": 0,
       "uq": 0, "dq": 0, "tq": 0}
qt_set = 0
qt = int(input())
while qt != 0:
    """quantidade de carta por tipo de carta
    exemplo: uc = um circulo, tt = tres triangulos"""

    for i in range(qt):
        dic["".join([i[0] for i in input().split(" ")])] += 1

    # sets com cartas de mesmo numero e simbolo
    for i in ['u', 'd', 't']:
        for j in ['c', 'q', 't']:
            quant = dic[i + j] // 3
            qt_set += quant
            dic[i + j] -= quant * 3
    # print(qt_set)

    # sets com diferentes simbolos e numeros
    qt_set += subtrair("uc", "dq", "tt")
    qt_set += subtrair("uc", "dt", "tq")
    qt_set += subtrair("dc", "tq", "dt")
    qt_set += subtrair("dc", "tt", "dq")
    qt_set += subtrair("tc", "uq", "dt")
    qt_set += subtrair("tc", "ut", "dq")

    # sets com cartas de diferentes numeros e mesmo simbolo
    for i in ['c', 'q', 't']:
        qt_set += subtrair('u' + i, 'd' + i, 't' + i)
    # print(qt_set)

    # sets com cartas de diferentes sombolos e mesmo numero
    for i in ['u', 'd', 't']:
        qt_set += subtrair(i + 'c', i + 'q', i + 't')
    # print(qt_set)

    dic = {"uc": 0, "dc": 0, "tc": 0,
           "ut": 0, "dt": 0, "tt": 0,
           "uq": 0, "dq": 0, "tq": 0}
    print(qt_set)
    qt_set = 0
    qt = int(input())