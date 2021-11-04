########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa o 1º termo de uma PA e sua razão. O programa retorna os 10 primeiros termos dessa PA.
########

from numeros import ler_num_nat

def calcular_n_termos_pa(A1, r):
    i = 1
    An = A1
    termo = 10
    total_termos = 10
    while termo != 0:
        while termo > 0:
            print(f'{An}', end=' -> ')
            An = A1 + i*r
            i += 1
            termo -= 1
        print('pausa')
        print('Digite zero para encerrar')
        termo = ler_num_nat('Quantos termos deseja mostrar? ')
        total_termos += termo
    print(f'Total de termos mostrados: {total_termos}')
