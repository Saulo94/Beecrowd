set_yes = set()
maior_nome = ""
lista_no = []

entrada = input()
while entrada != "FIM":
    nome, resposta = entrada.split()
    if resposta == "YES" and nome not in set_yes:
        set_yes.add(nome)
        if len(nome) > len(maior_nome):
            maior_nome = nome
    elif resposta == "NO":
        lista_no.append(nome)
    entrada = input()

for yes in sorted(set_yes):
    print(yes)
for no in sorted(lista_no):
    print(no)

print("\nAmigo do Habay:\n{0}".format(maior_nome))
