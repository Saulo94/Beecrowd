n = int(input())

if n % 2 == 0:
    n += 1

for x in range(2, n, 2):
    print(str(x) + "^2 = " + str(x ** 2))