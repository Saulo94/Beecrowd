def embaralhamento(tamanho):
    metade = tamanho // 2
    if tamanho == 2:
        return 2
    numero = 2
    movimentos = 0
    while numero != 1:
        if numero <= metade:
            numero *= 2
        else:
            numero = (numero - metade) * 2 - 1
        movimentos += 1
    return movimentos + 1


print(embaralhamento(int(input())))