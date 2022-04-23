qt = int(input())
qd, qf = 0, 0

for _ in range(qt):
    numero = int(input())
    if (numero >= 10) and (numero <= 20):
        qd += 1
    else:
        qf += 1

print(qd, " in")
print(qf, " out")
