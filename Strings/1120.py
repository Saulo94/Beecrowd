novo_numero_lista = []
digito_falho, numero = input().split()

while digito_falho != "0" and numero != "0":

    novo_numero_lista.clear()
    for digito in numero:
        if digito != digito_falho:
            novo_numero_lista.append(digito)
    
    novo_numero = "".join(novo_numero_lista)
    print(int(novo_numero) if novo_numero else "0")

    digito_falho, numero = input().split()
