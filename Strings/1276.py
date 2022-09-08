lista_alfabetica = list("abcdefghijklmnopqrstuvwxyz")

texto = set(input())

while True:

    lista_intervalo = []
    ultima_letra = ""

    for i, letra in enumerate(lista_alfabetica):
        if letra not in texto:
            continue
        if ultima_letra != lista_alfabetica[i - 1]:
            lista_intervalo.append([letra, letra, 1])
        else:
            lista_intervalo[-1][1] = letra
            lista_intervalo[-1][2] += 1
        ultima_letra = letra
    
    print(", ".join([":".join(intervalo[:2]) 
                    for intervalo in sorted(lista_intervalo)]))

    try:
        texto = set(input())
    except EOFError:
        break
