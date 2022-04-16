qt_bancos, qt_debentures = map(int, input().split())

while qt_bancos or qt_debentures:
    eh_possivel = True
    reservas = [0] + [int(reserva) for reserva in input().split()]

    for _ in range(qt_debentures):
        devedor, credor, debenture = map(int, input().split())
        reservas[devedor] -= debenture
        reservas[credor] += debenture
    for reserva in reservas[1:]:
        if reserva < 0:
            eh_possivel = False
            break
    if eh_possivel:
        print('S')
    else:
        print('N')

    qt_bancos, qt_debentures = map(int, input().split())
