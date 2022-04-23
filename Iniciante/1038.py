precos = {'1': 4, '2': 4.5, '3': 5, '4': 2, '5': 1.5}

cod, quant = list(float(i) for i in input().split())

print("Total: R$ {:.2f}".format(precos[cod] * quant))
