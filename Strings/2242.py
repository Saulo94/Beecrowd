vogais = {'a', 'e', 'i', 'o', 'u'}

risada = input()
risada_n = ''

for i in range(len(risada)):
    if risada[i] in vogais:
        risada_n += risada[i]

print("S" if risada_n == risada_n[::-1] else "N")
