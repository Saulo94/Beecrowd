n = int(input())

for _ in range(n):
    inicio, qtd_passos = map(int, input().split())

    if inicio % 2 == 0:
        inicio += 1
    
    print(sum(range(inicio, inicio + 2 * qtd_passos, 2)))
