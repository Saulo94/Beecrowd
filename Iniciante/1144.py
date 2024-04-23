# numero de entrada
n = int(input())

for i in range(1, n + 1):
    x, y, z = i, i ** 2, i ** 3
    print(x, y, z)
    print(x, y + 1, z + 1)
