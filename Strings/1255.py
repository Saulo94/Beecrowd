from collections import defaultdict

# lista de letras
letras = set(list("abcdefghijklmnopqrstuvwxyz"))

# quantidade de casos
qt_casos = int(input())

for _ in range(qt_casos):

    # dicionário de frequência por letra
    quantidade_by_letra = defaultdict(int)
    # conjunto de letras com a maior frequência
    letras_maior = set()
    # maior frequência
    maior_frequencia = 0

    for letra in input().lower():
        # se não for letra, ignora
        if letra not in letras:
            continue
        
        # incrementa a quantidade
        quantidade_by_letra[letra] += 1

        if quantidade_by_letra[letra] > maior_frequencia: # reseta o conjunto
            letras_maior = set([letra])
            maior_frequencia = quantidade_by_letra[letra]
        elif quantidade_by_letra[letra] == maior_frequencia: # adicionado no conjunto
            letras_maior.add(letra)

    print("".join(sorted(letras_maior)))
