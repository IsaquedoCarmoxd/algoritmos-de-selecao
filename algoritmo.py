import timeit
import random

def busca_binaria(lista_ordenada,elemento_procurado):
    primeiro = 0
    ultimo = len(lista_ordenada)-1

    while primeiro <= ultimo:
        meio = (primeiro+ultimo)//2
        atual = lista_ordenada[meio]

        if atual< elemento_procurado:
            primeiro = meio +1

        elif atual>elemento_procurado:
            ultimo = meio - 1

        else:
            return meio

    return None

def busca_simples(lista_ordenadada,elemento_procurado):
    for indice,elemento in enumerate(lista_ordenadada):
        if elemento==elemento_procurado:
            return indice
    return None

def selection_sort(lista):
    #algoritmo para ordenação de listas por seleção
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j,n):
            if lista[i]<lista[min_index]:
                min_index = i

        if lista[j]>lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i  in range(n-1):
            if lista[i] > lista[i+1]:
                #troca de elementos da posição i e i+1
                lista[i],lista[i+1] = lista[i+1],lista[i]
    return lista

def criacao_lista_ord(total):
    #criação de lista ordenada
    a = []
    for i in range(total):
        a.append(i)
    return a
def criacao_lista_random(total_elementos,min=1,max=1000):
    #criação de lista randomica, arrumar possivel falha de digitação(max menor q minimo e vice versa)
    lista = random.sample(range(min,max),total_elementos)
    return lista

a = criacao_lista_random(42,500)
print(bubble_sort(a))

            







"""
totais = [100, 1000,10000,100000,1000000,10000000,100000000]

for total in totais:
    minhalista = range(total)

    t_busca_simples = timeit.timeit(
        'busca_simples(minhalista,total-1)',
        number=10,
        globals=globals()
    )
    t_busca_binaria = timeit.timeit(
        'busca_binaria(minhalista,total-1)',
        number=10,
        globals=globals()
    )

    t_busca_simples = locals.__format__(
        "%5.8f",
        t_busca_simples/10,
        grouping = True
        )
    t_busca_binaria = locals.__format__(
        "%1.8f",
        t_busca_binaria/10,
        grouping = True
        )

print(
    f'Lista de {total:12n} elementos:\n'
    f'Tempo busca simples {t_busca_simples} segundos. \n'
    f'Tempo busca binaria {t_busca_binaria} segundos. \n'
) """





