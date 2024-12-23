# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
48°C - Selada
54°C - Ao ponto para o mal
60°C - Ao ponto
65°C - Ao ponto para o bem
71°C - Bem passada
'''

def ponto_do_steak(temperatura):
    if temperatura >= 48 and temperatura < 54:
        return 'Selada'
    elif temperatura >= 54 and temperatura < 60:
        return 'Ao ponto para o mal'
    elif temperatura >= 60 and temperatura < 65:
        return 'Ao ponto'
    elif temperatura >= 65 and temperatura < 71:
        return 'Ao ponto para o bem'
    elif temperatura >= 71:
        return 'Bem passada'
    else:
        return 'Carne crua'

temp = int(input('Qual a temperatura da carne? '))

print(ponto_do_steak(temp))