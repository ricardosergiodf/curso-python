def somar():
    print('Somar')

def multiplicar():
    print('Multiplicar')

def procura_index(lista, item):
    for i, valor in enumerate(lista):
        if valor == item:
            return i
    return -1
