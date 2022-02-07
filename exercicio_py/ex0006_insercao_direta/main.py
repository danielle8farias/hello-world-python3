from insertion_sort import insertion_sort
from random import sample

lista_desordenada = sample(range(1,50),10)

if __name__ == '__main__':
    print(f'Lista desordenada: {lista_desordenada}')
    lista_ordenada = insertion_sort(lista_desordenada)
    print(f'Agora a lista está ordenada: {lista_ordenada}')
