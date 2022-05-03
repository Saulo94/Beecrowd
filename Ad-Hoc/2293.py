linhas, colunas = map(int, input().split())

maior = 0
matriz = []
for i in range(linhas):
    matriz.append(list(map(int, input().split())))
    soma = sum(matriz[-1])
    if soma > maior:
        maior = soma
for i in range(colunas):
    soma = 0
    for k in range(linhas):
        soma += matriz[k][i]
    if soma > maior:
        maior = soma

print(maior)
