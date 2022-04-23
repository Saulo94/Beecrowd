qut_regiao = int(input())

while qut_regiao:
    # Lista de areas a ser copiada
    lista = list(range(1, qut_regiao + 1))
    # Salto a ser iterado
    salto = 0
    while True:
        # Lista de areas a ser manipulada
        areas = list(lista)
        salto += 1
        i = 0
        while len(areas) > 1:
            # Caso a area 13 não seja a última eliminada
            if areas[i] == 13:
                break
            # Caso o salto ultrapasse o tamanho da lista
            if i + salto > len(areas) - 1:
                del(areas[i])
                i = (i - 1 + salto) % len(areas)
            else:
                del(areas[i])
                i = i - 1 + salto
        if len(areas) == 1:
            print(salto)
            break
    qut_regiao = int(input())
