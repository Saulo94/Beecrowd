dic = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

quat_num = int(input())
for i in range(quat_num):
    num = input()
    soma = 0
    for k in num:
        soma += dic[k]

    print(str(soma) + " leds")
