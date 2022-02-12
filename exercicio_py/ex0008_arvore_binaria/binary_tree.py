class Vertice:
    def __init__(self, dado):
        self.dado = dado
        self.esquerdo = None
        self.direito = None

    def __str__(self):
        return str(self.dado)


class ArvoreBinaria:
    def __init__(self, dado=None):
        if dado:
            vertice = Vertice(dado)
            self.raiz = vertice
        else:
            self.raiz = None

    # percurso em ordem simétrica
    def in_ordem (self, vertice=None):
        if vertice is None:
            vertice = self.raiz
        if vertice.esquerdo:
            print('(', end='')
            self.in_ordem(vertice.esquerdo)
        print(vertice, end='')
        if vertice.direito:
            self.in_ordem(vertice.direito)
            print(')', end='')


if __name__ == "__main__":
    arvore = ArvoreBinaria()
    n1 = Vertice('A')
    n2 = Vertice('+')
    n3 = Vertice('*')
    n4 = Vertice('B')
    n5 = Vertice('-')
    n6 = Vertice('/')
    n7 = Vertice('C')
    n8 = Vertice('D')
    n9 = Vertice('E')

    n6.esquerdo = n7
    n6.direito = n8
    n5.esquerdo = n6
    n5.direito = n9
    n3.esquerdo = n4
    n3.direito = n5
    n2.esquerdo = n1
    n2.direito = n3

    arvore.raiz = n2

    arvore.in_ordem()
    print()
    