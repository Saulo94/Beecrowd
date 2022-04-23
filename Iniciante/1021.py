num = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    print("{0:.0f} nota(s) de R$ {1:.2f}".format(num // nota, nota))
    num %= nota
print("MOEDAS:")
for moeda in moedas:
    print("{0:.0f} moeda(s) de R$ {1:.2f}".format(num // moeda, moeda))
    num %= moeda
