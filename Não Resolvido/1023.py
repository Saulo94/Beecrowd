from collections import defaultdict

qt_imoveis = int(input())
i_cid = 0
while True:
    i_cid += 1
    total_consumo, total_pessoas = 0, 0
    dict_consumo = defaultdict(int)

    for pessoas, consumo in (map(int, input().split()) for _ in range(qt_imoveis)):
        total_pessoas += pessoas
        total_consumo += consumo
        dict_consumo[consumo // pessoas] += pessoas

    print("Cidade# {0}:\n"
          "{1}\n"
          "Consumo medio: {2:.2f} m3.".
          format(i_cid,
                 " ".join("{0}-{1}".format(dict_consumo[cons], cons) for cons in sorted(dict_consumo)),
                 int(total_consumo * 100 / total_pessoas) / 100))

    qt_imoveis = int(input())
    if not qt_imoveis:
        break
    else:
        print("")
