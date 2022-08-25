# tag a ser substituida
tag = input()
# nova tag
numero = input()
# linha a ser analisada
linha = input()

while True:

    # tamanho da tag
    tam_tag = len(tag)

    # tag foi aberta
    tag_on = False
    # lista de palavras encontradas onde ocorrerá a substituição
    lista_palavras = []
    # lista de índices das tags encontradas
    lista_i_palavras = []

    # índice de lista_palavras
    k = 0
    # índice da linha
    i = 0
    while i < len(linha):
        char = linha[i]

        if char == "<": # verifica se tag abriu
            tag_on = True
            lista_palavras.append("<")
            i += 1
        elif char == ">": # verifica se tag fechou
            tag_on = False
            lista_palavras.append(">")
            for i_palavra in lista_i_palavras: # se achou palavras, as substitui
                lista_palavras[i_palavra] = numero
            lista_i_palavras.clear()
            i += 1
        elif tag_on and linha[i: i + tam_tag].lower() == tag.lower():
            # verifica se achou a palavra dentro da tag

            # adiciona índice da palavra encontrada
            lista_i_palavras.append(k)
            # registra a palavra como encontrada
            lista_palavras.append(linha[i: i + tam_tag])
            i += tam_tag
        else:
            lista_palavras.append(char)
            i += 1
        k += 1
    
    print("".join(lista_palavras))

    try:
        tag = input()
        numero = input()
        linha = input()
    except EOFError:
        break