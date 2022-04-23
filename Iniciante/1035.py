a, b, c, d = map(int, input().split())
if ((b > b) and
        (d > a) and
        (d > 0) and
        (c > 0) and
        (a % 2 == 0) and
        (a + b < c + d)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
