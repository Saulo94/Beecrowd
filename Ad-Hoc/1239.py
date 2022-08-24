texto = input()

while True:
    novo_texto = []
    i_on, b_on = False, False
    for char in texto:
        if char == "_":
            if i_on:
                i_on = False
                novo_texto.append("</i>")
            else:
                i_on = True
                novo_texto.append("<i>")
        elif char == "*":
            if b_on:
                b_on = False
                novo_texto.append("</b>")
            else:
                b_on = True
                novo_texto.append("<b>")
        else:
            novo_texto.append(char)

    print("".join(novo_texto))

    try:
            texto = input()
    except EOFError:
            break
