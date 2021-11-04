########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Diversas operações com progressão aritmética.
########

from mensagem import ler_cabecalho, criar_rodape
from manipular_arquivos import abrir_arquivo
from interface import escolher_operacao
from numeros import ler_num_int, ler_num_nat
from n_termos_pa import calcular_n_termos_pa
from termo_pa import pa_termo
from pa_soma import pa_soma

from time import sleep

start = True

while start:
    ler_cabecalho('progressão aritmética')
    #abrindo arquivo de opções
    operacao = abrir_arquivo('opcoes.txt')
    opcao = escolher_operacao(operacao)

    # 10 primeiro termos de uma PA
    if opcao == 1:
        sleep(0.5)
        print(f'\nA operação escolhida foi:\n')
        ler_cabecalho(f'{operacao[opcao - 1]}')
        A1 =  ler_num_int('\nPrimeiro termo: ')
        r = ler_num_int('Razão: ')
        calcular_n_termos_pa(A1, r)

    elif opcao == 2:
        sleep(0.5)
        print(f'\nA operação escolhida foi:\n')
        ler_cabecalho(f'{operacao[opcao - 1]}')
        A1 =  ler_num_int('\nPrimeiro termo: ')
        r = ler_num_int('Razão: ')
        n = ler_num_nat('Termo: ')
        An = pa_termo(A1, r, n)
        sleep(0.5)
        print(f'\nA[{n}] = {An}')

    elif opcao == 3:
        sleep(0.5)
        print(f'\nA operação escolhida foi:\n')
        ler_cabecalho(f'{operacao[opcao - 1]}')
        A1 =  ler_num_int('\nPrimeiro termo: ')
        r = ler_num_int('Razão: ')
        n = ler_num_nat('Termo: ')
        soma = pa_soma(A1, r, n)
        sleep(0.5)
        print(f'\nSoma dos {n} termos = {soma}')

    elif opcao == 4:
        sleep(0.5)
        print('\nFinalizando o app')
        sleep(0.5)
        criar_rodape()
        sleep(0.5)
        start = False

    else:
        print('\nEscolha uma opção válida!')
