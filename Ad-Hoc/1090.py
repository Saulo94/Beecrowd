qt = int(input())
while qt != 0:
    # quantidade de cartas por tipo de carta
    dic = {"uc": 0, "dc": 0, "tc": 0,
           "ut": 0, "dt": 0, "tt": 0,
           "uq": 0, "dq": 0, "tq": 0}
    qt_set = 0

    for i in range(qt):
        dic["".join([i[0] for i in input().split(" ")])] += 1

    for i in ['u', 'd', 't']:
        for j in ['c', 'q', 't']:
            qt_set += dic[i+j] // 3

    for i in ['c', 'q', 't']:
        qt_set += min(dic['u'+i], dic['d'+i], dic['t'+i])

    for i in ['u', 'd', 't']:
        qt_set += min(dic[i+'c'], dic[i+'q'], dic[i+'t'])

    qt_set += min(dic["uc"], dic["dq"], dic["tt"])
    qt_set += min(dic["uc"], dic["dt"], dic["tq"])
    qt_set += min(dic["dc"], dic["uq"], dic["tt"])
    qt_set += min(dic["dc"], dic["ut"], dic["tq"])
    qt_set += min(dic["tc"], dic["dq"], dic["uc"])
    qt_set += min(dic["tc"], dic["dc"], dic["uq"])

    print(qt_set)

    qt = int(input())
