from collections import defaultdict
letras = ["A", "B", "C", "D", "E"]

qt_senhas = int(input())
i_teste = 0
while qt_senhas:
    i_teste += 1
    senha = {}
    for _ in range(qt_senhas):
        entrada = input().split()
        digito_by_letra = defaultdict(set)
        for i, digito in enumerate(entrada[:10]):
            digito_by_letra[letras[i // 2]].add(digito)
        for i, letra in enumerate(entrada[10:]):
            if senha.get(i):
                senha[i] = senha[i] & digito_by_letra[letra]
            else:
                senha[i] = digito_by_letra[letra]

    senha_nova = []
    for i in range(6):
        senha_nova.append(list(senha[i])[0])
    print("Teste {0}\n{1}\n".format(i_teste, " ".join(senha_nova) + " "))

    qt_senhas = int(input())
