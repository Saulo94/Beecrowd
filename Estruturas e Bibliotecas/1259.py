quat_numero = int(input())
lista_impares, lista_pares = [], []

for _ in range(quat_numero):
    numero = int(input())
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

for i in sorted(lista_pares):
    print(i)
for i in sorted(lista_impares, reverse=True):
    print(i)
