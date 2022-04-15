frase = input()

while frase != '*':
    eh_tautograma = True
    letras = set()
    for palavra in frase.split():
        letras.add(palavra[0].lower())
        if len(letras) > 1:
            eh_tautograma = False
            break
    if eh_tautograma:
        print('Y')
    else:
        print('N')

    frase = input()
