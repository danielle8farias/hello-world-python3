########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função recebe como argumentos o 1º termo de uma PA, sua razão e o número de termos. 
# O programa retorna o An termo.
########

def pa_termo(A1, r, n):
    An = A1 + (n-1) * r
    return An


def test_pa():
    assert pa_termo(0, 3, 10) == 27

def test_pa1():
    assert pa_termo(1, 8, 21) == 161

def test_pa2():
    assert pa_termo(2020, -5, 13) == 1960
