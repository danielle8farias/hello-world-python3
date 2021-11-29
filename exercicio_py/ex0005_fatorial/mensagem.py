########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Funções para:
#           ler e criar um cabeçalho;
#           criar um rodapé;
########

def ler_cabecalho(msg):
    '''
    recebe uma string e retorna a mesma em caixa alta com espaçamento de 50 caracteres, incluindo a string passada.
    linha pontilhada em baixo e em cima.
    '''
    print('-'*50)
    print(f'{msg.upper():^50}')
    print('-'*50)


def criar_rodape():
    '''
    sem parâmetro
    retorna a string FIM com espaçamento de 50 caracteres, incluindo a string.
    linha pontilhada em baixo e em cima.
    '''
    print('-'*50)
    print(f'{str.upper("fim"):^50}')
    print('-'*50)
