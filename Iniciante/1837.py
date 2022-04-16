n1, n2 = map(int, input().split())

if n1 > 0 and n2 > 0:
    quociente = n1 // n2
    resto = n1 % n2
elif n1 > 0 and n2 < 0:
    quociente = -(n1 // -n2)
    resto = n1 % -n2
elif n1 < 0 and n2 > 0:
    quociente = n1 // n2
    resto = n1 - n2 * quociente
else:
    quociente = n1 // n2
    if n1 != n2 * quociente:
        quociente += 1
    resto = n1 - n2 * quociente

print("{0} {1}".format(quociente, resto))
