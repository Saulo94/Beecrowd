quat_ing = int(input())
i_teste = 0
while quat_ing != 0:
    i_teste += 1
    for i, num in enumerate(map(int, input().split())):
        if i + 1 == num:
            print("Teste {0}\n{1}\n".format(i_teste, i + 1))
            break
    quat_ing = int(input())
