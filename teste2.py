def isContido(parte, lista):
    if parte in lista:
        print(f'{parte} contém em {lista}') # printa se contém
        return True
    else:
        print(f'{parte} não contém em {lista}') #printa se não contém
        return False
    
lista = ['toyota', 'honda', 'ford', 'tesla']
string = 'honda'
lista2 = [1,2,3,4]

print(isContido('honda', lista)) # chama a função com os dois parametros
print(isContido('volkswagen', lista))
print(isContido('honda', string))
print(isContido(2, lista2))
print(isContido(5, lista2))