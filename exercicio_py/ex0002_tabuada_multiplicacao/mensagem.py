########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Funções para:
#           ler e criar um cabeçalho;
#           criar um rodapé;
#           criar linha;
#           ler e validar resposta se deseja continuar
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


def criar_linha(tam=50):
    '''
    sem parâmetro.
    retorna sinais de = repetidos em 50 caracteres.
    '''
    print()
    print('-'*tam)
    print()


def ler_resposta(msg):
    '''
    Aceita que o usuário digite apenas S/SIM ou N/Não
    '''
    while True:
        try:
            resposta = input(msg).upper().strip()[0]
            if resposta not in 'SN':
                raise Exception('S para sim ou N para não')
        except IndexError:
            print(f'Resposta inválida.')
            continue
        except Exception as erro:
            print(f'Resposta inválida: {erro}')
            continue
        else:
            return resposta
