#!/usr/bin/env python3.8

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Jogo da forca. 
#           Usuário seleciona um tema e o programa escolhe uma palavra aleatória de um arquivo referente a esses temas.
#           Programa retorna o número de letras da palavra escolhida e usuário escolhe uma letra por ver para tentar adivinhar a palavra.
#           Ao adivinhar a letra, o programa a coloca em sua posição na palavra. Ao errar, o programa armazena a letra errada e coloca um membro do bonequinho na forca.
#           O usuário ganha se adivinhar todas as letras que compõe a palavra e perde se completar todos os membros do bonequinho.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape

from interface import escolher_tema, desenhar_forca
from manipular_arquivos import abrir_arquivo
from palavra_pc import escolher_palavra, palavra_secreta, adivinhar_palavra

from time import sleep

jogando = True

while jogando:
    ler_cabecalho('jogo da forca')
    #abrindo arquivo de temas
    temas = abrir_arquivo('temas.txt')
    opcao = escolher_tema(temas)
    #frutas
    if opcao == 1:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1]}')
        #abrindo arquivo com nome de frutas
        lista_frutas = abrir_arquivo('frutas.txt')
        #recebendo retorno de palavra escolhida e tamanho
        fruta_escolhida, tamanho = escolher_palavra(lista_frutas)
        #recebendo retorno de palavra secreta
        palavra_oculta = palavra_secreta(tamanho)
        adivinhar_palavra(tamanho, palavra_oculta, fruta_escolhida)
    #cores
    elif opcao == 2:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1]}')
        #abrindo arquivo com nome das cores
        lista_cores = abrir_arquivo('cores.txt')
        #recebendo retorno de palavra escolhida e tamanho
        cor_escolhida, tamanho = escolher_palavra(lista_cores)
        #recebendo retorno de palavra secreta
        palavra_oculta = palavra_secreta(tamanho)
        adivinhar_palavra(tamanho, palavra_oculta, cor_escolhida)
    #planetas
    elif opcao == 3:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1]}')
        #abrindo arquivo com nome dos planetas
        lista_planetas = abrir_arquivo('planetas.txt')
        #recebendo retorno de palavra escolhida e tamanho
        planeta_escolhido, tamanho = escolher_palavra(lista_planetas)
        #recebendo retorno de palavra secreta
        palavra_oculta = palavra_secreta(tamanho)
        adivinhar_palavra(tamanho, palavra_oculta, planeta_escolhido)
    #capitais brasileiras
    elif opcao == 4:
        sleep(0.5)
        print(f'\nO tema escolhido foi:')
        ler_cabecalho(f'{temas[opcao - 1]}')
        #abrindo arquivo com nome das capitais brasileiras
        lista_capitais = abrir_arquivo('capitais_br.txt')
        #recebendo retorno de palavra escolhida e tamanho
        capital_escolhida, tamanho = escolher_palavra(lista_capitais)
        #recebendo retorno de palavra secreta
        palavra_oculta = palavra_secreta(tamanho)
        adivinhar_palavra(tamanho, palavra_oculta, capital_escolhida)
    elif opcao == 5:
        sleep(0.5)
        print('Finalizando o jogo')
        sleep(0.5)
        criar_rodape()
        sleep(0.5)
        jogando = False
    else:
        print('Escolha uma opção válida!')
