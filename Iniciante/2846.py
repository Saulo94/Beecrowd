alvo = int(input())
ultimos_numeros = [1, 1]
k_fibonot = 0

numero = 2
while True:
    if numero == (ultimos_numeros[0] + ultimos_numeros[1]):
        ultimos_numeros[0], ultimos_numeros[1] = ultimos_numeros[1], numero
    else:
        k_fibonot += 1
        if k_fibonot == alvo:
            print(numero)
            break
    numero += 1
