def comportamento(sequencia):
    dif = sequencia[1] - sequencia[0]
    for i, num in enumerate(sequencia[1:]):
        nova_dif = num - sequencia[i]
        if nova_dif * dif < 0:
            return "N"
        else:
            dif = nova_dif
    return "D" if dif < 0 else "C"


print(comportamento(list(map(int, input().split()))))
