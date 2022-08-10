dias = int(input().split()[1])
horas, min, seg = map(int, input().split(" : "))

# tempo inicial
tempo_i = dias * 24 * 3600 + horas * 3600 + min * 60 + seg

dias = int(input().split()[1])
horas, min, seg = map(int, input().split(" : "))

# tempo final
tempo_f = dias * 24 * 3600 + horas * 3600 + min * 60 + seg

diferenca = tempo_f - tempo_i

print(str(diferenca // (24 * 3600)) + " dia(s)")
diferenca -= (diferenca // (24 * 3600)) * 24 * 3600
print(str(diferenca // 3600) + " hora(s)")
diferenca -= (diferenca // 3600) * 3600
print(str(diferenca // 60) + " minuto(s)")
diferenca -= (diferenca // 60) * 60
print(str(diferenca) + " segundo(s)")
