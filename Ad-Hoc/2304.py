dinheiro, qt_ope = list(map(int, input().split()))
jogadores = {"D": dinheiro, "E": dinheiro, "F": dinheiro}

for i in range(qt_ope):
    acao, pessoa, quantia = input().split()

    if acao == "C":
        jogadores[pessoa] -= int(quantia)
    elif acao == "V":
        jogadores[pessoa] += int(quantia)
    else:
        jogadores[pessoa] += int(quantia)
        jogadores[pessoa] -= int(quantia)

print(jogadores["D"], jogadores["E"], jogadores["F"])
