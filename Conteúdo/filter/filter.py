numeros = [10,12,34,44,57]

def remover20(x):
    return x>20

print(list(filter(remover20, numeros))) # filtrando somente o que der True

print(list(filter(lambda x: x>20, numeros)))