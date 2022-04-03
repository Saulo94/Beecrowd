from math import log

qt_teste = int(input())

for _ in range(qt_teste):
    p1, p2, g1, g2 = input().split()
    p1, p2, g1, g2 = int(p1), int(p2), float(g1), float(g2)

    t = 0
    while p1 <= p2 and t <= 100:
        p1 += int((g1 / 100) * p1)
        p2 += int((g2 / 100) * p2)
        t += 1

    if t == 101:
        print("Mais de 1 seculo.")
    else:
        print(t, "anos.")