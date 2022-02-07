def insertion_sort(lista):
    # pegando o tamanho da lista a ser ordenada
    tamanho_lista = len(lista)
    # comparação a partir do segundo elemento da lista,
    #   pois uma lista de 1 elemento já está ordenada.
    # o range vai até "tamanho_lista-1" elementos, pois o intervalo é aberto
    for i in range(1, tamanho_lista):
        # pegando o elemento na posição de "i" para cada iteração do "for"
        elemento = lista[i]
        # "j" é a posição a esquerda da lista
        j = i - 1
        # enquanto o índice do elemento for maior ou igual a 0
        #   e o elemento da posição a esquerda for maior do que o elemento
        #   a ser analisado nessa iteração do "for" acima...
        while j >= 0 and lista[j] > elemento:
            # ...deve-se avançar a posição atual;
            #   elemento da posição a esquerda vai para a direita.
            lista[j+1] = lista[j]
            j -= 1
            lista[j+1] = elemento
    return lista
