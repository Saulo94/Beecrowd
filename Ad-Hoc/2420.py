quantidade_int = int(input())

lista_int = list(map(int, input().split()))
soma_i, soma_j = 0, 0
i, j = 0, quantidade_int - 1

while i <= quantidade_int - 1 and j > 0:
    if i == j:
        print(i)
        break
    elif soma_i + lista_int[i] <= soma_j + lista_int[j]:
        soma_i += lista_int[i]
        i += 1
    else:
        soma_j += lista_int[j]
        j -= 1
