def ordenar_lista_menor_mayor(lista:list, indice:int = 0):
    '''brief: ordena una lista de listas de menor a mayor segun el indice

    lista: lista de listas\n
    indice: indice de la lista a ordenar

    retorno: no retorna nada
    '''
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice] > lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista_mayor_menor(lista:list, indice:int = 0):
    '''brief: ordena una lista de listas de mayor a menor segun el indice

    lista: lista de listas\n
    indice: indice de la lista a ordenar

    retorno: no retorna nada
    '''
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice] < lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux