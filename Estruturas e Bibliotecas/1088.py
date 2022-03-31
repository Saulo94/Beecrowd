class No:
    def __init__(self, valor):
        self.valor = valor
        self.conteudo = 1
        self.filho_esquerdo = None
        self.filho_direito = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def add(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            return 0
        else:
            return self.adicionar_elemento(self.raiz, valor)

    def adicionar_elemento(self, no, valor):
        if no.valor > valor:
            if no.filho_esquerdo is None:
                no.filho_esquerdo = No(valor)
                return no.conteudo
            else:
                return no.conteudo + self.adicionar_elemento(no.filho_esquerdo, valor)
        else:
            no.conteudo += 1
            if no.filho_direito is None:
                no.filho_direito = No(valor)
                return 0
            else:
                return self.adicionar_elemento(no.filho_direito, valor)


entrada = [int(i) for i in input().split()]
while entrada[0] != 0:
    arvore = Arvore()
    soma = 0
    for numero in entrada[1:]:
        soma += arvore.add(numero)
    if soma % 2 == 0:
        print("Carlos")
    else:
        print("Marcelo")
    entrada = [int(i) for i in input().split()]
