########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número inteiro e programa retorna a tabuada de multiplicação desse.
########

from mensagem import *
from numeros import ler_num_nat
from tabuada import Tabuada

ler_cabecalho('tabuada de multiplicação')

while True:
    num_usr = ler_num_nat('Digite um número: ')
    num = Tabuada(num_usr)
    num.criar_tabuada()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
