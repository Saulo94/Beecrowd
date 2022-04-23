tr = sorted(list(map(float, input().split())))

if tr[0] >= tr[1] + tr[2]:
    print("NAO FORMA TRIANGULO")
else:
    if tr[0] * tr[0] == tr[1] * tr[1] + tr[2] * tr[2]:
        print("TRIANGULO RETANGULO")
    elif tr[0] * tr[0] > tr[1] * tr[1] + tr[2] * tr[2]:
        print("TRIANGULO OBTUSANGULO")
    elif tr[0] * tr[0] < tr[1] * tr[1] + tr[2] * tr[2]:
        print("TRIANGULO ACUTANGULO")
    if (tr[0] == tr[1]) and (tr[0] == tr[2]):
        print("TRIANGULO EQUILATERO")
    elif (tr[0] == tr[1]) or (tr[0] == tr[2]) or (tr[1] == tr[2]):
        print("TRIANGULO ISOSCELES")
