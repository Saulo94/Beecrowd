formato = "{0:.1f}"
soma, operacao = 0, input()
for linha in range(12):
    for coluna in range(12):
        numero = float(input())
        if linha < coluna < 11 - linha:
            soma += numero
print(formato.format(soma / 30)) if operacao == 'M' else print(formato.format(soma))
