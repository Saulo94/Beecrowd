from itertools import product


def checar_quadrantes(matriz):
    intervalos = [range(0, 3), range(3, 6), range(6, 9)]
    for int_lin, int_col in product(intervalos, intervalos):
        set_quadrante = set()
        for i in int_lin:
            for k in int_col:
                if matriz[i][k] in set_quadrante:
                    return False
                else:
                    set_quadrante.add(matriz[i][k])
    return True


def checar_linhas(matriz):
    for k in range(9):
        matriz.append([])
        set_linha = set()

        for numero in map(int, input().split()):
            if numero in set_linha:
                return False
            else:
                matriz[k].append(numero)
    return True


def checar_colunas(matriz):
    for j in range(9):
        set_colunas = set()
        for linha in matriz:
            if linha[j] in set_colunas:
                return False
            else:
                set_colunas.add(linha[j])
    return True


quat_matriz = int(input())
for i in range(1, quat_matriz + 1):
    matriz = []

    print("Instancia", i)
    if checar_linhas(matriz) and checar_colunas(matriz) and checar_quadrantes(matriz):
        print("SIM")
    else:
        print("NAO")
    print("")
