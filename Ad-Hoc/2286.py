quat_part = int(input())
teste = 1

while quat_part != 0:
    nome1, nome2 = input(), input()

    print("Teste", teste)
    lista_jog = []
    for _ in range(quat_part):
        valor1, valor2 = map(int, input().split())

        if (valor1 + valor2) % 2 == 0:
            print(nome1)
        else:
            print(nome2)
    print("")

    quat_part = int(input())
    teste += 1
