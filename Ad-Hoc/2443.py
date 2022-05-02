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


num1, den1, num2, den2 = map(int, input().split())

num = num1 * den2 + num2 * den1
den = den1 * den2

print(*simplificacao(num, den))
