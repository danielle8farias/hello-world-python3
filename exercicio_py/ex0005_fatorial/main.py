########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna o seu fatorial.
########

from mensagem import ler_cabecalho, criar_rodape
from manipular_arquivos import abrir_arquivo
from interface import escolher_operacao
from numeros import ler_num_nat
from fatoriais import fatorial_detalhado, fatorial_simples
from time import sleep


start = True
while start:
    ler_cabecalho('fatorial')
    #abrindo arquivo de opções
    lista_opcao = abrir_arquivo('opcoes.txt')
    opcao = escolher_operacao(lista_opcao)

    # 10 primeiro termos de uma PA
    if opcao == 1:
        sleep(0.5)
        print(f'\nA operação escolhida foi:\n')
        ler_cabecalho(f'{lista_opcao[opcao - 1]}')
        num = ler_num_nat('Digite um número natural: ')
        print(fatorial_detalhado(num))
        print()
        sleep(1)
    elif opcao == 2:
        sleep(0.5)
        print(f'\nA operação escolhida foi:\n')
        ler_cabecalho(f'{lista_opcao[opcao - 1]}')
        num = ler_num_nat('Digite um número natural: ')
        print(f'Fatorial = {fatorial_simples(num)}')
        print()
        sleep(1)
    elif opcao == 3:
        sleep(0.5)
        print('\nFinalizando o app')
        sleep(0.5)
        criar_rodape()
        sleep(0.5)
        start = False
    else:
        print('\nEscolha uma opção válida!')
