########
# autora: danielle8farias@gmail.com
# repositório: https://github.com/danielle8farias
# Descrição: Abre o arquivo com opções e retorna os itens numa lista.
########

def abrir_arquivo(nome):
    '''
    Abre o arquivo do tema escolhido pelo usuário e retorna os itens numa lista.
    '''
    arq = open(nome, 'rt')

    lista_itens = []
    for linha in arq:
        # removendo quebra de linha dos arquivos
        # pode ser usado o strip() para retirar a quebra de linha
        item = linha.replace('\n', '')
        # criando uma lista dos dados do arquivo
        lista_itens.append(item)

    arq.close()
    return lista_itens
