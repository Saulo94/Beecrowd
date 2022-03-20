class No:
    def __init__(self, valor, conteudo):
        self.valor = valor
        self.conteudo = conteudo
        self.filho_direito = None
        self.filho_esquerdo = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def add(self, valor, conteudo):
        if self.raiz is None:
            self.raiz = No(valor, [conteudo])
        else:
            self.adicionar_elemento(valor, conteudo, self.raiz)

    def adicionar_elemento(self, valor, conteudo, no):
        if no.valor == valor:
            no.conteudo.append(conteudo)
        elif no.valor > valor:
            if no.filho_esquerdo is None:
                no.filho_esquerdo = No(valor, [conteudo])
            else:
                self.adicionar_elemento(valor, conteudo, no.filho_esquerdo)
        elif no.valor < valor:
            if no.filho_direito is None:
                no.filho_direito = No(valor, [conteudo])
            else:
                self.adicionar_elemento(valor, conteudo, no.filho_direito)

    def printar_conteudo_ordenado_por_valor(self):
        lista_palavras = self.printar(self.raiz)
        print(*lista_palavras)

    def printar(self, no):
        if no.filho_esquerdo is not None and no.filho_direito is not None:
            return self.printar(no.filho_direito) + no.conteudo + self.printar(no.filho_esquerdo)
        if no.filho_esquerdo is None and no.filho_direito is not None:
            return self.printar(no.filho_direito) + no.conteudo
        if no.filho_esquerdo is not None and no.filho_direito is None:
            return no.conteudo + self.printar(no.filho_esquerdo)
        if no.filho_esquerdo is None and no.filho_direito is None:
            return no.conteudo


qt = int(input())
for _ in range(qt):
    arvore_palavras = Arvore()
    palavras = input().split()
    for palavra in palavras:
        arvore_palavras.add(len(palavra), palavra)
    arvore_palavras.printar_conteudo_ordenado_por_valor()