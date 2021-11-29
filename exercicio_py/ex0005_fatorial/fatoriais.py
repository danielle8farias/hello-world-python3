########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Cálculo dos fatoriais.
########

from time import sleep


def fatorial_detalhado(num):
    print(f'\nCalculando {num}!')
    f = 1
    sleep(0.5)
    for i in range(num, 0, -1):
        # i vai assumir o valor de num dentro do laço
        if i > 1:
            print(f'{i} x ', end='', flush=True)
            sleep(0.5)
        else:
            print(f'{i} = ', end='', flush=True)
            sleep(0.5)
        f *= i
    return f


def fatorial_simples(n):
    if n == 1 or n == 0:
        return 1
    # recursão
    return fatorial_simples(n-1) * n
