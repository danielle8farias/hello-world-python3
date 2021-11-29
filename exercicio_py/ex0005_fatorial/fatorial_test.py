########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: função que recebe um número inteiro e retorna o seu fatorial.
########

def fat(n):
    fat = 1
    if n == 1 or n == 0:
        return fat
    else:
        for i in range(n, 0, -1):
            fat *= i
        return fat



#testes
def test_fat():
    assert fat(5) == 120

def test_fat1():
    assert fat(1) == 1

def test_fat2():
    assert fat(8) == 40320
