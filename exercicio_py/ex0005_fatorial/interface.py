########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Menu inicial de opções do fatorial.
########

from numeros import ler_num_nat


def escolher_operacao(lista_opcao):
    '''
    Cria o menu e retorna a opção escolhida
    '''
    c = 1
    for item in lista_opcao:
        print(f'{c} - {item}')
        c += 1
    print()
    opcao = ler_num_nat('Escolha um opcao: ')
    return opcao
