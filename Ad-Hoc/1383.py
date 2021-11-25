quat_matriz = int(input())
lista_final = []
i = 0
while i < quat_matriz:
    res = True
    matriz = []
    for j in range(9):
        matriz.append(list(int(k) for k in input().split()))
        lista_sub = list(matriz[-1])
        lista_sub.sort()
        if lista_sub != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            res = False

    if res:
        lista_sub = []
        j = 0
        while j < 9:
            for k in matriz:
                lista_sub.append(k[j])
            lista_sub.sort()
            if lista_sub != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                res = False
                break
            else:
                lista_sub = []
            j += 1
    if res:
        i_l = [[0, 2], [3, 5], [6, 8]]
        i_c = [[0, 2], [3, 5], [6, 8]]
        for j in i_l:
            for k in i_c:
                lista_sub = []
                l = j[0]
                while l <= j[1]:
                    c = k[0]
                    while c <= k[1]:
                        lista_sub.append(matriz[l][c])
                        c += 1
                    l += 1
                lista_sub.sort()
                if lista_sub != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    res = False
                    break
            if not res:
                break
    if res:
        lista_final.append([i + 1, "SIM"])
    else:
        lista_final.append([i + 1, "NAO"])
    i += 1
for i in lista_final:
    print("Instancia " + str(i[0]))
    print(i[1])
    print("")