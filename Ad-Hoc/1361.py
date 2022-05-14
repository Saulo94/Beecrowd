def quantidade_piso(lista_):
    i = 0
    while i < len(lista_) - 1:
        if lista_[i][1] == lista_[i + 1][1]:
            del(lista_[i])
            i = 0
        else:
            i += 1
    return len(lista_)


quat_teste = int(input())
for _ in range(quat_teste):
    quat_piso = int(input())
    lista_piso = []
    for _ in range(quat_piso):
        piso = int(input())
        if piso < 0:
            lista_piso.append([piso * -1, 0])
        else:
            lista_piso.append([piso, 1])
    lista_piso.sort()
    print(quantidade_piso(lista_piso))
