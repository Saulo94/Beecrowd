cartas = list(map(int, input().split()))

if (cartas[0] == cartas[1]) or (cartas[0] > cartas[1]):
    print(cartas[0])
else:
    print(cartas[1])
