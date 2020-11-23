''' Algoritmo de pesquisa binária. Este algoritmo é aplicado
    em uma lista ordenada e terá um número x de etapas dependendo
    do tamanho da lista.
'''

def pesquisa_binaria(lista, item):
    baixo = 0 # Onde inicia a lista
    alto = len(lista) - 1 # O final da lista
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    return None

minha_lista = [1, 3, 5, 7, 9]

# Mostra  a posição onde está o elemento buscado (caso exita) ou retorna None
print(pesquisa_binaria(minha_lista, 9))
print(pesquisa_binaria(minha_lista, -1))