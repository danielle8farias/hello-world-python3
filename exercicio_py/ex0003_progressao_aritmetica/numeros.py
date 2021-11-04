########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Funções para:
#           validar números naturais;
#           validar número inteiro;
########


def ler_num_nat(n):
    '''
    aceita somente números naturais
    '''
    while True:
        try:
            num = int(input(n))
            if num < 0:
                raise Exception('Digite um número maior ou igual a zero.')
        except ValueError:
            print('Apenas números naturais.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return num


def ler_num_int(n):
    '''
    Valida números inteiros positivos ou negativos.
    '''
    while True:
        try:
            num = int(input(n))
        except ValueError:
            print('Digite um número inteiro!')
            continue
        else:
            return num
