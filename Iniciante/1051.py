val = float(input())

if val <= 2000:
    print('Isento')
elif (val > 2000) and (val <= 3000):
    print("R$ {:.2f}".format((val-2000)*0.08))
elif (val > 3000) and (val <= 4500):
    print("R$ {:.2f}".format(((val-3000)*0.18) + 80))
else:
    print("R$ {:.2f}".format(((val - 4500) * 0.28) + 350))
