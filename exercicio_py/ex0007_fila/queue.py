from node import Noh

class Queue:
    def __init__(self):
        self.tamanho_fila = 0
        self.primeiro = None
        self.ultimo = None


    # insere um elemento na fila
    def inserir(self, elemento):
        noh = Noh(elemento)

        # se a fila estiver vazia
        if self.ultimo is None:
            # ultimo elemento acabou de chegar
            self.ultimo = noh
        # se já existir alguém na fila como último elemento
        else:
            self.ultimo.proximo = noh
            self.ultimo = noh

        # se a fila estiver vazia
        if self.primeiro is None:
            # primeiro elemento acabou de chegar
            self.primeiro = noh

        # incrementado a fila
        self.tamanho_fila += 1


    # remover um elemento da fila
    #   filas só removem da posição inicial
    def remover(self):
        # verificando se a posição inicial não é vazia
        if self.primeiro is not None:
            # pegando o dado do primeiro elemento da fila
            elemento_saida = self.primeiro.valor
            # reduzindo o tamanho da fila
            self.tamanho_fila -= 1
            # o elemento seguinte ocupa a primeira posição
            self.primeiro = self.primeiro.proximo
            return elemento_saida
        raise IndexError('A fila está vazia')


    # retorna o primeiro da fila sem remover
    def quem_primeiro(self):
        if self.primeiro is not None:
            # pegando o dado do primeiro elemento da fila
            elemento_saida = self.primeiro.valor
            return elemento_saida
        raise IndexError('A fila está vazia')


    def __len__(self):
        return self.tamanho_fila


    def __repr__(self):
        if self.tamanho_fila > 0:
            fila = ''
            ponteiro = self.primeiro
            # enquanto != None
            while(ponteiro):
                fila = fila + str(ponteiro.valor) + ' - '
                ponteiro = ponteiro.proximo
            return fila
        return 'A fila está vazia'
