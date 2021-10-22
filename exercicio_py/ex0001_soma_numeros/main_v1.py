########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita dois números inteiros e programa retorna a soma entre eles.
########

#função lambda:
#   funciona semelhante a uma função
#   lambda recebe_valor(es) : retorno da função
somar = (lambda x, y: x + y)

#condicional:
#   invocar as chamadas abaixo somente se esse script for executado diretamente
if __name__ == '__main__':
    print(somar(4, 3))
    print(somar(3.4, 2.1))
