########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função para validar número float;
########

def ler_num_float(n):
    '''
    Validação todo o conjuntos dos números reais
    '''
    while True:
        try:
            num = float(input(n))
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            return num
