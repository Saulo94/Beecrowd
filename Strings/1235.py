qt_casos = int(input())

for _ in range(qt_casos):
    texto = input()

    tamanho = len(texto)
    metade = tamanho // 2

    novo_texto = list(" " * tamanho)

    i = metade - 1
    j = metade
    k = 0
    l = tamanho - 1
    while i >= 0:
        novo_texto[k] = texto[i]
        novo_texto[l] = texto[j]
        i -= 1
        j += 1
        k += 1
        l -= 1
    
    print("".join(novo_texto))
