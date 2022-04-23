def operacao(op, num1, den1, num2, den2):
    if op == '+':
        resultado = num1 * den2 + num2 * den1, den1 * den2
    elif op == '-':
        resultado = num1 * den2 - num2 * den1, den1 * den2
    elif op == '*':
        resultado = num1 * num2, den1 * den2
    else:
        resultado = num1 * den2, num2 * den1
    return resultado


def simplificacao(num, den):
    mdc = None
    while mdc != 1:
        # algoritmo de euclides (mdc)
        # a = b * n + r
        a, b = abs(num), abs(den)
        if a < b:
            a, b = b, a
        r = a % b
        while r != 0:
            a, b = b, r
            r = a % b
        mdc = b
        num /= mdc
        den /= mdc
    return int(num), int(den)


qt_operacoes = int(input())
for _ in range(qt_operacoes):
    entrada = input().split()
    num1, den1, num2, den2, op = int(entrada[0]), int(entrada[2]), int(entrada[4]), int(entrada[6]), entrada[3]

    res = operacao(op, num1, den1, num2, den2)
    simp = simplificacao(res[0], res[1])

    print("{0}/{1} = {2}/{3}".format(res[0], res[1], simp[0], simp[1]))
