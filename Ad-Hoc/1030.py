def quem_sobrou(lista, passo, index_inicio):
    tam = len(lista)
    while tam != 1:
        if index_inicio >= tam:
            index_inicio %= tam
        lista.pop(index_inicio)
        index_inicio += passo - 1
        tam = len(lista)
    return lista[0]


qt_teste = int(input())

for i in range(qt_teste):
    pessoas, passo = map(int, input().split())
    lista_pessoas = list(range(1, pessoas + 1))
    print("Case {0}: {1}".format(i + 1, quem_sobrou(lista_pessoas, passo, passo - 1)))
