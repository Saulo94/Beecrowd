qt_pinos, altura = map(int, input().split())

lista = list(map(int, input().split()))

deslocamento = 0
passos = 0
i = 0
while i < qt_pinos - 1:
    if lista[i] != altura:
        if lista[i] >= altura:
            deslocamento = lista[i] - altura
            lista[i] = altura
            lista[i + 1] -= deslocamento
            passos += deslocamento
        else:
            deslocamento = altura - lista[i]
            lista[i] = altura
            lista[i + 1] += deslocamento
            passos += deslocamento
    i += 1

print(passos)
