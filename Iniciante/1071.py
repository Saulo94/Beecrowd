n1, n2 = int(input()), int(input())
if n1 > n2:
    n1, n2 = n2, n1

soma = sum([numero for numero in range(n1 + 1, n2) if numero % 2 == 1])

print(soma)
