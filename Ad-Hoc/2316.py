l_c = list(map(int, input().split()))

matriz = []
maior = 0
for i in range(l_c[0]):
    matriz.append(list(map(int, input().split())))

    if i == 0:
        maior = sum(matriz[-1])
    elif i != 0 and sum(matriz[-1]) > maior:
        maior = sum(matriz[-1])

i = 0
while i < l_c[1]:
    k = 0
    soma = 0
    while k < l_c[0]:
        soma += matriz[k][i]
        k += 1
    if soma > maior:
        maior = soma
    i += 1

print(maior)
