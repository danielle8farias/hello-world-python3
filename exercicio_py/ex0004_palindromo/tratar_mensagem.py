########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: tratando palavra a ser verificada como palíndromo
########

def ler_frase(frase):
    msg = input(frase).strip().lower()
    # transformando a mensagem em uma lista
    lista_palavras = msg.split()
    # unindo a lista de palavras em uma nova string, sem espaços
    msg_junto = ''.join(lista_palavras)
    return msg_junto
