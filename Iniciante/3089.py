quat_n = int(input())

while quat_n != 0:
    presentes = list(int(i) for i in input().split())
    maior_s = presentes[0] + presentes[-1]
    menor_s = presentes[0] + presentes[-1]
    del (presentes[0], presentes[-1])
    while presentes:
        soma_s = presentes[0] + presentes[-1]
        if soma_s > maior_s:
            maior_s = soma_s
            maior_p = soma_s
        elif soma_s < menor_s:
            menor_p = soma_s
            menor_s = soma_s
        del (presentes[0], presentes[-1])
    print(maior_s, menor_s)
    quat_n = int(input())
