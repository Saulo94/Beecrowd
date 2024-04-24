from math import ceil

x = int(input())

z = x

while z <= x:
    z = int(input())

# equação de 2º grau para encontrar
delta = ((2 * x - 1) ** 2 + 8 * z) ** (1 / 2)

n1 = (-(2 * x - 1) + delta) / 2
n2 = (-(2 * x - 1) - delta) / 2

# pegar o menor número positivo
if n1 > 0 and n2 > 0:
    n = ceil(min(n1, n2))
else:
    n = ceil(max(n1, n2))

if ((2 * x + n - 1) * n) // 2 == z:
    n += 1

print(n)
