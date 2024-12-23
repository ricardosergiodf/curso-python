# Podem ser usados: try, except, else, finally

try:
    marcas = ['toyota', 'vw', 'fiat', 'honda']
    print(marcas[4])
except IndexError:
    print('Index não existe')