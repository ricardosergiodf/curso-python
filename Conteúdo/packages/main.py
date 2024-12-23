# import funcoes # -> importa tudo que está no arquivo funcoes
from funcoes import somar, multiplicar # -> importa somente as funções escolhidas do arquivo funcoes
from items.cadastro import cliente # -> importa somente o cadastro de cliente do package items

somar()
multiplicar()

cliente()