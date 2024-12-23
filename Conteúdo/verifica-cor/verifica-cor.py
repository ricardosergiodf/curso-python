# Verificar se uma cor ou cores está em estoque

coresEstoque = ['amarelo', 'verde', 'azul', 'vermelho', 'branco', 'preto', 'cinza']

def isCorEmEstoque(*cores):
    coresEmEstoque = []
    coresSemEstoque = []
    for cor in cores:
        if coresEstoque.__contains__(cor):
            print(f'{cor} contém no estoque.')
            coresEmEstoque.append(cor)
        else:
            print(f'{cor} não contém no estoque.')
            coresSemEstoque.append(cor)
    print(f'Cores em estoque: {coresEmEstoque}')
    print(f'Cores sem estoque: {coresSemEstoque}')

isCorEmEstoque('amarelo', 'marrom', 'azul', 'branco')