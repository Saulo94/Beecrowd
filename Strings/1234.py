frase = input()

while True:
    nova_palavra = []
    i = 0
    for char in frase:
        if char != ' ':
            if i % 2 == 0:
                nova_palavra.append(char.upper())
            else:
                nova_palavra.append(char.lower())
            i += 1
        else:
            nova_palavra.append(' ')

    print("".join(nova_palavra))

    try:
        frase = input()
    except EOFError:
        break
