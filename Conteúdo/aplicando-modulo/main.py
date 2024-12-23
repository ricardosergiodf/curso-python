# verificar se algo está na lista e retornar ele e seu index

from funcoes import procura_index

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = procura_index(list1, 'b')
var2 = procura_index(list1, 'w')
print(var1)
print(var2)