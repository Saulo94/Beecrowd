def quantidade_s(dimensao):
    quat_quadrado = 0
    for i in range(lado, 0, -1):
        quat_quadrado += i ** dimensao
    return quat_quadrado


lado = int(input())
while lado >= 0:
    s2 = quantidade_s(2)
    s3 = quantidade_s(3)
    s4 = quantidade_s(4)
    r2 = int((lado + 1) * lado / 2 * (lado + 1) * lado / 2 - s2)
    r3 = int((lado + 1) * lado / 2 * (lado + 1) * lado / 2 * (lado + 1) * lado / 2 - s3)
    r4 = int((lado + 1) * lado / 2 * (lado + 1) * lado / 2 * (lado + 1) * lado / 2 * (lado + 1) * lado / 2 - s4)
    print(s2, r2, s3, r3, s4, r4)
    try:
        lado = int(input())
    except EOFError:
        break
