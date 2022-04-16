formato = "{0:.1f}"
soma, operacao = 0, input()
for linha in range(12):
    for coluna in range(12):
        numero = float(input())
        if coluna > linha:
            soma += numero
print(formato.format(soma / 66)) if operacao == 'M' else print(formato.format(soma))
