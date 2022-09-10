qt_casos = int(input())

desloc_3_dir = lambda char: chr(ord(char) + 3)

desloc_1_esq = lambda char: chr(ord(char) - 1)

letras = set(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

for _ in range(qt_casos):

    # texto criptografado
    novo_texto = []

    # passada 1
    for char in input():
        novo_texto.append(desloc_3_dir(char) if char in letras else char)

    metade = len(novo_texto) // 2

    # passada 3 no texto invertido
    for i, char in enumerate(novo_texto[::-1]):
        novo_texto[i] = desloc_1_esq(char) if i >= metade else char
    
    print("".join(novo_texto))
