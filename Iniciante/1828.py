possibilidades = {"tesoura": {"papel", "lagarto"}, "papel": {"pedra", "Spock"}, "pedra": {"lagarto", "tesoura"},
                  "lagarto": {"Spock", "papel"}, "Spock": {"tesoura", "pedra"}}
formato = "Caso #{0}: {1}!"

qt_teste = int(input())
for i in range(1, qt_teste + 1):
    sheldon, raj = input().split()
    if raj in possibilidades[sheldon]:
        print(formato.format(i, "Bazinga"))
    elif sheldon in possibilidades[raj]:
        print(formato.format(i, "Raj trapaceou"))
    else:
        print(formato.format(i, "De novo"))
