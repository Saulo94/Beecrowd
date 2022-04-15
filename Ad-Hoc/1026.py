num1, num2 = ("{0:b}".format(int(numero))[::-1] for numero in input().split())

while True:
    if len(num1) > len(num2):
        num2 = (num2 + '0' * (len(num1) - len(num2)))
    else:
        num1 = (num1 + '0' * (len(num2) - len(num1)))

    numero = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            numero += 2**i
    print(numero)

    # EOFError
    try:
        num1, num2 = ("{0:b}".format(int(numero))[::-1] for numero in input().split())
    except EOFError:
        break
