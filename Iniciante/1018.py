num = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(num)
for nota in notas:
    print("{0} nota(s) de R$ {1},00".format(num // nota, nota))
    num %= nota
