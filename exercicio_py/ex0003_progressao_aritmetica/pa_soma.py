########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Função recebe como argumentos o 1º termo de uma PA, sua razão e o número de termos. Retorna a soma de todos esses termos.
########

from termo_pa import pa_termo

def pa_soma(A1, r, n):
    An = pa_termo(A1, r, n)
    soma = (A1 + An) * n/2
    return soma
