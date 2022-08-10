quant_pos = 0
soma = 0

for x in range(6):
    numero = float(input())
    if numero > 0:
        quant_pos += 1
        soma += numero

print(quant_pos, "valores positivos")
print("%.1f" % (soma / quant_pos))