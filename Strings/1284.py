"""Problema 1284"""

def get_qtd_cliques(palavra: str, outras_palavras: list) -> int:
    """retorna a quantidade de cliques para a palavra"""

    qtd_cliques = 0

    # lista de palavras com mesmas letras
    novas_outras_palavras = []

    for i, letra in enumerate(palavra):
        # se for primeira iteração, não resete a lista
        if i > 0:
            outras_palavras = tuple(novas_outras_palavras)
        
        # limpa a lista para novas palavras com mesmas letras
        novas_outras_palavras.clear()

        # qtd de palavras com letra diferente
        qtd_palavras_diferentes = 0

        # itera outras palavras para achar aquelas com mesmas letras
        for outra_palavra in outras_palavras:
            if len(outra_palavra) <= i or letra != outra_palavra[i]:
                qtd_palavras_diferentes += 1
            else:
                novas_outras_palavras.append(outra_palavra)
        
        if i == 0:
            qtd_cliques += 1

            if qtd_palavras_diferentes == len(outras_palavras):
                break
            if qtd_palavras_diferentes == 0:
                continue
        else:
            if qtd_palavras_diferentes == len(outras_palavras):
                qtd_cliques += 1
                break
            if qtd_palavras_diferentes == 0:
                continue
            qtd_cliques += 1

    return qtd_cliques
    

def get_media_cliques(num_palavras: int) -> float:
    """retorna a média de cliques"""
    
    palavras = []

    # lê as palavras
    for _ in range(num_palavras):
        palavras.append(input())
    
    lista_qtd_cliques = []
    for i, palavra in enumerate(palavras):
        qtd_cliques = get_qtd_cliques(palavra, [item for k, item in enumerate(palavras) if k != i])
        
        lista_qtd_cliques.append(qtd_cliques)

    return sum(lista_qtd_cliques) / len(lista_qtd_cliques)


lista_medias_cliques = []

while True:
    try:
        media_cliques = get_media_cliques(int(input()))
    except EOFError:
        break
    
    lista_medias_cliques.append(f"{media_cliques:0.2f}")

print("\n".join(lista_medias_cliques))
