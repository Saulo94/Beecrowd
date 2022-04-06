from collections import defaultdict

qt_imoveis = int(input())
lista_prints = []
index = 1
while True:
    total_consumo, total_pessoas = 0, 0
    dict_consumo = defaultdict(int)

    for _ in range(qt_imoveis):
        pessoas, consumo = map(int, input().split())
        total_pessoas += pessoas
        total_consumo += consumo
        dict_consumo[consumo // pessoas] += pessoas

    qt_imoveis = int(input())
    if qt_imoveis:
        lista_prints.append("Cidade# {0}:\n"
                            "{1}\n"
                            "Consumo medio: {2:.2f} m3.\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons)
                                            for cons in sorted(dict_consumo)),
                                   int(total_consumo * 100 / total_pessoas) / 100))
        index += 1
    else:
        lista_prints.append("Cidade# {0}:\n"
                            "{1}\n"
                            "Consumo medio: {2:.2f} m3.\n".
                            format(index,
                                   " ".join("{0}-{1}".format(dict_consumo[cons], cons)
                                            for cons in dict_consumo),
                                   int(total_consumo * 100 / total_pessoas) / 100))
        break

print("\n".join(lista_prints))