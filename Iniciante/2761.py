from struct import unpack, pack


def quantidade_decimal(numero):
    return len(numero) - (len(str(round(float(numero), None))) + 1)


def espaço_certo(variavel):
    if len(variavel) >= 10:
        return variavel
    else:
        return (" " * (10 - len(variavel))) + variavel


var1, var2, var3, var4 = input().split(" ", 3)
decimal = quantidade_decimal(var2)
sub = (unpack('f', pack('f', float(var2)))[0])
var2 = ('{:.' + str(decimal) + 'f}').format(round(sub, decimal))
print(var1 + var2 + var3 + var4)
print(var1 + "\t" + var2 + "\t" + var3 + "\t" + var4)
print(espaço_certo(var1) + espaço_certo(var2) + espaço_certo(var3) + espaço_certo(var4))
