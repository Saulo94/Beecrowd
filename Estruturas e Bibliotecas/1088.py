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
        else:
            self.adicionar_elemento(self.raiz, valor)

    def adicionar_elemento(self, no, valor):
        if no.valor > valor:
            no.conteudo += 1
            if no.filho_esquerdo is None:
                no.filho_esquerdo = No(valor)
            else:
                self.adicionar_elemento(no.filho_esquerdo, valor)
        else:
            if no.filho_direito is None:
                no.filho_direito = No(valor)
            else:
                self.adicionar_elemento(no.filho_direito, valor)

    def quant_menores(self, valor):
        if self.raiz is None:
            return 0
        else:
            return self.verificar_quantidade_menores(self.raiz, valor)

    def verificar_quantidade_menores(self, no, valor):
        if no.valor > valor:
            if no.filho_esquerdo is None:
                return 0
            else:
                return self.verificar_quantidade_menores(no.filho_esquerdo, valor)
        else:
            if no.filho_direito is None:
                return no.conteudo
            else:
                return no.conteudo + self.verificar_quantidade_menores(no.filho_direito, valor)


entrada = [int(i) for i in input().split()]
while entrada[0] != 0:
    arvore = Arvore()
    soma = 0
    for numero in entrada[entrada[0]:0:-1]:
        soma += arvore.quant_menores(numero)
        arvore.add(numero)
    if soma % 2 == 0:
        print("Carlos")
    else:
        print("Marcelo")

    entrada = [int(i) for i in input().split()]
