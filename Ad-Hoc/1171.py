def inserir_ordenadamente(lista, numero):
    tam = len(lista)
    if tam == 0:
        lista.append(numero)
        return lista
    meio = tam // 2
    item = lista[meio]
    if meio == 0:
        if numero > item:
            lista.insert(meio + 1, numero)
        else:
            lista.insert(meio, numero)
        return lista
    else:
        if numero > item:
            return lista[:meio] + inserir_ordenadamente(lista[meio:], numero)
        else:
            return inserir_ordenadamente(lista[:meio], numero) + lista[meio:]


qt = int(input())

frequencia = {}
lista_ordenada = []

for _ in range(qt):
    numero = int(input())
    try:
        frequencia[numero] += 1
    except Exception as e:
        frequencia[numero] = 1
        lista_ordenada = inserir_ordenadamente(lista_ordenada, numero)

for numero in lista_ordenada:
    print("{0} aparece {1} vez(es)".format(numero, frequencia[numero]))