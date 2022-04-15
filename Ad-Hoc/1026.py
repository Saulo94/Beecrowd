num1, num2 = ("{0:b}".format(int(numero)) for numero in input().split())

while True:
    if len(num1) > len(num2):
        num2 = ('0' * (len(num1) - len(num2)) + num2)[::-1]
        num1 = num1[::-1]
    else:
        num1 = ('0' * (len(num2) - len(num1)) + num1)[::-1]
        num2 = num2[::-1]

    numero = 0
    i = 0
    while i < len(num1):
        if num1[i] != num2[i]:
            numero += 2**i
        i += 1
    print(numero)

    # EOFError
    try:
        num1, num2 = ("{0:b}".format(int(numero)) for numero in input().split())
    except EOFError:
        break
