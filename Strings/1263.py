texto = input()

while True:

    ultima_letra = ""
    registrou_aliteracao = False
    qt_aliteracoes = 0

    for palavra in texto.lower().split(" "):
        if palavra[0] == ultima_letra:
            if not registrou_aliteracao:
                registrou_aliteracao = True
                qt_aliteracoes += 1
        else:
            registrou_aliteracao = False
            ultima_letra = palavra[0]
    
    print(qt_aliteracoes)


    try:
        texto = input()
    except EOFError:
        break
