########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Teste da função que recebe dois números e retorna a soma entre eles. Usando PyTest.
########

def somar(n1, n2):
    return n1 + n2


#testes
def test_soma():
    assert somar(1,2) == 3

def test_soma1():
    assert somar(5,5) == 10

def test_soma2():
    assert somar(7,2) == 9
