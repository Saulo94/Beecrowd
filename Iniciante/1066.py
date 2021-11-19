par, impar, pos, neg = 0, 0, 0, 0

for x in range(5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(pos) + " valor(es) positivo(s)")
print(str(neg) + " valor(es) negativo(s)")