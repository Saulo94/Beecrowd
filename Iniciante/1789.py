qt_lesmas = int(input())

while True:

    maior_velocidade = 0
    for lesma in map(int, input().split()):
        if lesma > maior_velocidade:
            maior_velocidade = lesma

    if maior_velocidade < 10:
        print('1')
    elif maior_velocidade < 20:
        print('2')
    else:
        print('3')

    try:
        qt_lesmas = int(input())
    except EOFError:
        break
