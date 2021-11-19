animais = {"C": 0, "R": 0, "S": 0}

for i in range(int(input())):
    count, sigla = input().split(" ")
    animais[sigla] += int(count)

total = sum(animais.values())
print("Total: {0} cobaias".format(total))
print("Total de coelhos: {0}".format(animais["C"]))
print("Total de ratos: {0}".format(animais["R"]))
print("Total de sapos: {0}".format(animais["S"]))
print("Percentual de coelhos: {:.2f} %".format(animais["C"] / total * 100))
print("Percentual de ratos: {:.2f} %".format(animais["R"] / total * 100))
print("Percentual de sapos: {:.2f} %".format(animais["S"] / total * 100))
