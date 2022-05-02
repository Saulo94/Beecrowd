qt_postos, distancia = list(map(int, input().split()))
lista = list(map(int, input().split())) + [42195]

consegue = True
for i in range(qt_postos):
    if lista[i + 1] - lista[i] > distancia:
        consegue = False
        break

print("S" if consegue else "N")
