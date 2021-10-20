########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Funções para:
#           ler e criar um cabeçalho;
#           criar um rodapé;
#           criar linha;
#           ler e validar resposta se deseja continuar
#           validar recebimento de uma string formada apenas por letras.
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
            #[0] captura apenas o primeiro caractere da string
            #strip() remove os espaços no começo e no fim
            #upper() transforma string em maiúscula
            #input() captura o que é digitado
            #atribuindo valor à variável 'resposta'
            resposta = input(msg).upper().strip()[0]
            #verifica se não está contido na string 'SN';
            #   não há conflito, pois 'resposta' captura apenas a posição inicial da string
            if resposta not in 'SN':
                #criando exceção
                raise Exception('S para sim ou N para não')
        #em caso de resposta vazia; 
        #   caso não haja string para pegar a posição inicial
        except IndexError:
            print(f'Resposta inválida.')
            continue
        #chama a exceção criada
        #variável 'e' retorna a mensagem da exceção
        except Exception as erro:
            #print(f'') retorna uma string formatada na tela
            print(f'Resposta inválida: {erro}')
            #volta para o início do laço
            continue
        #se o 'try' for válido
        else:
            #retorna o valor da resposta
            return resposta


def ler_palavra(msg):
    '''
    Verifica se o que foi digitado foram apenas letras
    '''
    while True:
        try:
            palavra = input(msg).upper().strip()
            #retirando espaços
            palavras = palavra.split()
            palavras = ''.join(palavras)
            #isalpha() se possui apenas letras
            #verificando se palavra possui caracteres que não sejam letras
            if not palavras.isalpha():
                raise Exception('Digite apenas letras.')
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        #se o 'try' for válido
        else:
            return palavra

