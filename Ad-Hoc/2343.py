coordenadas = {}
qt = int(input())
resposta = 0
for _ in range(qt):
    x, y = input().split()
    if coordenadas.get((x, y)):
        resposta = 1
    else:
        coordenadas[(x, y)] = True
print(resposta)
