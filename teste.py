from datetime import date
def calculaDiasEntreDatas(data1, data2):
    if data1 > data2:
        return data1.day - data2.day # retorna a diferença de dias
    else:
        return data2.day - data1.day
    
#data1 = date(input('Digite a data 1: ')) # para usar o input, preciso colocar variavel dia, mes e ano
#data2 = date(input('Digita a data 2: '))

data1 = date(2014, 7, 2) # chama a função com os parametros da data
data2 = date(2014, 7, 11)

print(calculaDiasEntreDatas(data1, data2))