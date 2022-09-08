qt_casos = int(input())

pos_alfabeto_by_letra = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))

for _ in range(qt_casos):
    soma_hash = 0

    qt_palavras = int(input())

    for i_palavra in range(qt_palavras):
        for i, letra in enumerate(input()):
            soma_hash += pos_alfabeto_by_letra[letra] + i + i_palavra
    
    print(soma_hash)
