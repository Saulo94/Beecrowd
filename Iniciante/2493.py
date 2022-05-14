def encontrar_operacao(num1, num2, num3):
    if num1 + num2 == num3:
        return '+'
    elif num1 - num2 == num3:
        return '-'
    elif num1 * num2 == num3:
        return '*'
    else:
        return 'I'


qt_exp = int(input())
while True:
    errados = []
    operacoes = [0]
    for _ in range(qt_exp):
        num1, *resto = input().split()
        num2, num3 = resto[0].split("=")
        operacoes.append(encontrar_operacao(int(num1), int(num2), int(num3)))
    for _ in range(qt_exp):
        nome, ind, operador = input().split()

        if operacoes[int(ind)] != operador:
            errados.append(nome)

    if len(errados) == 0:
        print("You Shall All Pass!")
    elif len(errados) == qt_exp:
        print("None Shall Pass!")
    else:
        print(*sorted(errados))

    try:
        qt_exp = int(input())
    except EOFError:
        break
