n = int(input())

divisores = ['1']

for i in range(2, n // 2 + 1):
    if n % i == 0:
        divisores.append(str(i))

divisores.append(str(n))

print("\n".join(divisores))
