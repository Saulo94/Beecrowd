qt_palavras, max_lin_p_pag, max_char_lin = (int(n) for n in input().split())


def comparar_palavra(tam_palavra, qt_char, qt_lin, qt_pag):
    if qt_char + tam_palavra <= max_char_lin:
        qt_char += tam_palavra
    else:
        if qt_lin + 1 <= max_lin_p_pag:
            qt_lin += 1
            qt_char = tam_palavra - 1
        else:
            qt_pag += 1
            qt_lin = 1
            qt_char = tam_palavra - 1
    
    return qt_char, qt_lin, qt_pag

while True:

    qt_char = 0
    qt_lin = 1
    qt_pag = 1
    i_palavra = 0

    for palavra in input().split():
        tam_palavra = len(palavra)
        if i_palavra != 0:
            tam_palavra += 1
        else:
            i_palavra = 1
        
        qt_char, qt_lin, qt_pag = comparar_palavra(tam_palavra, 
                                                   qt_char, 
                                                   qt_lin, 
                                                   qt_pag)

    print(qt_pag)

    try:
        qt_palavras, max_lin_p_pag, max_char_lin = (int(n) for n in input().split())
    except EOFError:
        break
