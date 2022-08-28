qt_casos = int(input())

posicao_by_letra = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(65, 91)))

palavra_decodificada = []

for _ in range(qt_casos):
    
    palavra_decodificada.clear()
    palavra_codificada = input()

    qt_pulos = int(input())

    for digito in palavra_codificada:
        cod_digito = posicao_by_letra[digito]
        cod_digito -= qt_pulos
        if cod_digito < 65:
            cod_digito = 91 - (65 - cod_digito)
        palavra_decodificada.append(chr(cod_digito))
    
    print("".join(palavra_decodificada))
