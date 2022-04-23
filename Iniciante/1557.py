def mostrar_matriz(ordem):
    tamanho = str(len(str(4 ** (ordem - 1))))
    formato = "{:" + tamanho + "}"
    for i in range(ordem):
        print(*[formato.format(2 ** (i + k)) for k in range(ordem)])


numero = int(input())
while True:
    mostrar_matriz(numero)

    numero = int(input())
    if numero:
        print("")
    else:
        break
