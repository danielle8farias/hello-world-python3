class Nome:
    def __init__(self, nome):
        self.__nome = nome

    def imprimir_boas_vindas(self):
        print(f'Bem-vinda, {self.__nome}!')
        