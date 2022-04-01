from bisect import insort
from time import time


def truncar(decimal):
    p1, p2 = decimal.split(".")
    tam_p2 = len(p2)
    if tam_p2 >= 2:
        return p1 + "." + p2[:2]
    else:
        return p1 + "." + p2 + "0" * (2 - tam_p2)


lista_prints = []
qt_imoveis = int(input())
inicio = time()
index = 1
while True:
    dict_consumo = {}
    lista_consumo = []
    total_consumo = 0
    total_pessoas = 0

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
                            "Consumo medio: {2} m3.\n\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons) for cons in lista_consumo),
                                   truncar(str(total_consumo / total_pessoas))))
        index += 1
    else:
        lista_prints.append("Cidade# {0}:\n"
                            "{1}\n"
                            "Consumo medio: {2} m3.\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons) for cons in lista_consumo),
                                   truncar(str(total_consumo / total_pessoas))))
        break

print("".join(lista_prints))
print(time() - inicio)