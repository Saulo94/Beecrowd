from bisect import insort
from array import array
from time import time


lista_prints = []
qt_imoveis = int(input())
inicio = time()
index = 1
while True:
    dict_consumo = {}
    lista_consumo = array('I')
    total_consumo, total_pessoas = 0, 0

    for pessoas, consumo in (map(int, input().split()) for _ in range(qt_imoveis)):
        total_pessoas += pessoas
        total_consumo += consumo

        consumo_pessoa = consumo // pessoas
        if consumo_pessoa in dict_consumo:
            dict_consumo[consumo_pessoa] += pessoas
        else:
            dict_consumo[consumo_pessoa] = pessoas
            insort(lista_consumo, consumo_pessoa)

    qt_imoveis = int(input())
    if qt_imoveis:
        lista_prints.append("Cidade# {0}:\n"
                            "{1}\n"
                            "Consumo medio: {2:.2f} m3.\n\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons) for cons in lista_consumo),
                                   int(total_consumo * 100 / total_pessoas) / 100))
        index += 1
    else:
        lista_prints.append("Cidade# {0}:\n"
                            "{1}\n"
                            "Consumo medio: {2:.2f} m3.\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons) for cons in lista_consumo),
                                   int(total_consumo * 100 / total_pessoas) / 100))
        break

print("".join(lista_prints))
print((time() - inicio) * 100)