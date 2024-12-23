'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

def calcula_pintura(rend, alt, larg):
    area_parede = alt*larg
    qtde_latas = area_parede / rend
    return f'Você precisa de {qtde_latas} latas de tinta'

rendimento = float(input('Qual é o rendimento da lata? '))
altura = float(input('Qual é a altura da parede '))
largura = float(input('Qual é a largura da parede? '))

print(calcula_pintura(rendimento, altura, largura))