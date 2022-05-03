import numpy as np

linhas, colunas = map(int, input().split())
maior = 0
matriz = np.empty((linhas, colunas), dtype=np.uint32)
for i in range(linhas):
    matriz[i] = np.array(list(map(int, input().split())))
    soma = sum(matriz[i])
    if soma > maior:
        maior = soma

print(max(max(matriz.sum(axis=0)), maior))
