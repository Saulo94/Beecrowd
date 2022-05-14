vogais = {'a', 'e', 'i', 'o', 'u'}
alfabeto = list('abcdefghijklmnopqrstuvwxyz')
dict_alfabeto = dict((letra, i) for i, letra in enumerate(alfabeto))


def criptografar_texto(chave, texto):
    tam_chave, i_chave = len(chave) - 1, 0
    novo_texto = []
    for palavra in texto.split():
        if palavra[0] not in vogais:
            for letra in palavra:
                qt_deslocado = dict_alfabeto[chave[i_chave]]
                novo_texto.append((alfabeto[qt_deslocado:] + alfabeto[:qt_deslocado])[dict_alfabeto[letra]])
                i_chave = 0 if i_chave == tam_chave else i_chave + 1
        else:
            novo_texto.extend(list(palavra))
        novo_texto.append(" ")

    return "".join(novo_texto[:-1])


palavra_chave, qt_palavras = input(), int(input())
for _ in range(qt_palavras):
    print(criptografar_texto(palavra_chave, input()))
