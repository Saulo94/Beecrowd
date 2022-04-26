qt_casos = int(input())

for i in range(qt_casos):
    num1, num2 = input().split()
    if str(num2) == str(num1)[-len(num2):]:
        print("encaixa")
    else:
        print("nao encaixa")
