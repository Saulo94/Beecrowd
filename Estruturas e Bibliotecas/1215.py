from re import sub, match

set_palavras = set()
entrada = [sub(u'[^a-zA-Z]', " ", i).split() for i in input().split()]
while True:
    for palavra in entrada:
        if type(palavra) == list:
            for palavra2 in palavra:
                if match('^[a-zA-Z]+$', palavra2) is not None:
                    set_palavras.add(palavra2.lower())
        else:
            if match('^[a-zA-Z]+$', palavra) is not None:
                set_palavras.add(palavra.lower())
    try:
        entrada = [sub(u'[^a-zA-Z]', " ", i).split() for i in input().split()]
    except EOFError:
        break

for palavra in sorted(set_palavras):
    print(palavra)
