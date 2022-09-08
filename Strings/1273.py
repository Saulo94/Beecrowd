qt_palavras = int(input())

while True:
    lista_palavras = []
    maior_tamanho = 0
    for _ in range(qt_palavras):
        lista_palavras.append(input())
        tamanho_palavra = len(lista_palavras[-1])
        if tamanho_palavra > maior_tamanho:
            maior_tamanho = tamanho_palavra
    
    for palavra in lista_palavras:
        qt_espacos = maior_tamanho - len(palavra)
        print(" " * qt_espacos + palavra)
    
    qt_palavras = int(input())
    if qt_palavras:
        print("")
    else:
        break
