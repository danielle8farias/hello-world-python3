########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa uma palavra ou frase e programa retorna se ela é um palíndromo.
########


from mensagem import ler_cabecalho, criar_rodape, criar_linha, ler_resposta
from tratar_mensagem import ler_frase


ler_cabecalho('palíndrimo')

while True:
    msg = ler_frase('Digite uma frase: ')
    msg_inverso = ''
    tamanho = len(msg)

    # início: tamanho-1; para ir do último caractere a 0
    # fim: -1; para ir até a última string
    # passo: -1; decrescendo
    for letra in range(tamanho-1, -1, -1):
        # concatenando cada caractere detrás pra frente
        msg_inverso += msg[letra]

    if msg_inverso == msg:
        print('É um palíndromo!')
        print(f'O inverso da palavra é: {msg_inverso}')
    else:
        print('Não é palíndromo')
        print(f'O inverso da palavra é: {msg_inverso}')

    resposta = ' '
    while resposta not in 'SN':
        #chamada da função que faz a validação da resposta
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    #chamada da função que cria a linha pontilhada
    criar_linha()

criar_rodape()
