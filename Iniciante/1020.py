total = int(input())

ano = total // 365
mes = (total % 365) // 30
dia = (total % 365) % 30

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
