########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Abre o arquivo do tema escolhido pelo usuário e retorna os itens numa lista.
#           Recebe um inteiro referente ao tamanho da palavra escolhida e monta o número de letras que essa palavra possui. 
#           Faz a comparação entre a letra escolhida pelo usuário e as letras da palavra que foi escolhida pelo computador.
#           Registra os erros do usuário.
#           Retorna a vitória ou derrota do usuário. 
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_palavra

from interface import desenhar_forca

from random import choice
from time import sleep


def escolher_palavra(lista_palavras):
    '''
    Recebe uma lista de palavras e escolhe uma aleatoriamente
    '''
    palavra_escolhida = choice(lista_palavras)
    return palavra_escolhida, len(palavra_escolhida)


def palavra_secreta(tamanho):
    '''
    Recebe um inteiro referente ao tamanho da palavra escolhida e monta o número de letras que essa palavra possui.
    '''
    string_oculta = '__ '*tamanho
    return string_oculta


def adivinhar_palavra(tamanho, palavra_oculta, palavra_escolhida):
    '''
    Faz a comparação entre a letra escolhida pelo usuário e as letras da palavra que foi escolhida pelo computador.
    Registra os erros do usuário.
    Retorna a vitória ou derrota do usuário.
    '''
    erros = 0
    forca = desenhar_forca()
    lista_chutes = []
    lista_palavra_oculta = palavra_oculta.split()
    palavra_escolhida = palavra_escolhida.upper()
    #palavra que será lida pelo computador e usada para fazer a comparação
    nova_palavra1 = ' '
    #desenho da forca
    sleep(0.5)
    print(forca[erros])
    sleep(0.5)
    print(f'\nA palavra é: {palavra_oculta}')
    while (erros < 6) and (palavra_escolhida != nova_palavra1):
        sleep(0.5)
        chute = ler_palavra('\nEscolha uma letra: ')[0]
        posicao = 0

        if chute not in lista_chutes:
            lista_chutes.append(chute)

            if chute not in palavra_escolhida:
                erros += 1
                sleep(0.5)
                print(f'\nVocê tem {erros} erros.')
            else:
                for letra in palavra_escolhida:
                    if chute == letra:
                        sleep(0.5)
                        print(f'letra: {chute}, na posição: {posicao}')
                        lista_palavra_oculta[posicao] = chute
                    posicao += 1
                #palavra que é mostrada na tela para o usuário
                nova_palavra = ' '.join(lista_palavra_oculta)
                #palavra que será lida pelo computador e usada para fazer a comparação
                nova_palavra1 = ''.join(lista_palavra_oculta)

        else:
            sleep(0.5)
            print('Essa letra já foi escolhida!')
        
        sleep(0.5)
        #desenho da forca
        print(forca[erros])
        sleep(0.5)
        #caso o usuário erre antes de acertar uma primeira letra
        if nova_palavra1 == ' ':
            print(f'\nA palavra é: {palavra_oculta}')
        else:
            print(f'\nA palavra é: {nova_palavra}')
        sleep(0.5)
        print(f'\nLetras que já foram escolhidas: {lista_chutes}')

    if palavra_escolhida == nova_palavra1:
        print()
        sleep(0.5)
        print(f'*'*8,' PARABÉNS! VOCÊ VENCEU! ','*'*8)
        sleep(1.5)
        print()
    else:
        print()
        sleep(0.5)
        print(f'-'*8,' Você perdeu ','-'*8)
        sleep(1.5)
        print()
