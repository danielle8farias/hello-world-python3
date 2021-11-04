class Tabuada:
    def __init__(self, num):
        self.__num = num

    def criar_tabuada(self):
        i = 1
        for i in range(i, 10):
            print(f'{self.__num:4} x {i} = {self.__num * i}')
        print()
