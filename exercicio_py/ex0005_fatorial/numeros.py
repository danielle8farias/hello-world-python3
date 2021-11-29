########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Função para:
#           validar números naturais;
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
