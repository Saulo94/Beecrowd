qut_regiao = int(input())
lista_principal = []

while qut_regiao != 0:
    lista = []
    i = 0
    while i < qut_regiao:
        lista.append(i+1)
        i += 1
    res = False
    salto = 1
    while not res:
        lista_sub = list(lista)
        i = 0
        while len(lista_sub) > 1:
            if i + salto > len(lista_sub) -1:
                del(lista_sub[i])
                i = i - 1 + salto
                while i > len(lista_sub) - 1:
                    i -= len(lista_sub)
            else:
                del(lista_sub[i])
                i += salto - 1
        if lista_sub[0] == 13:
            res = True
            lista_principal.append(salto)
        salto += 1
    qut_regiao = int(input())
for i in lista_principal:
    print(i)