# Calculadora de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm?
Qual é o seu peso em kg?

MENOR QUE 18.5      MAGREZA
ENTRE 18.5 E 24.9   NORMAL
ENTRE 25.0 E 29.9   SOBREPESO
ENTRE 30.0 E 39.9   OBESIDADE
MAIOR QUE 40.0      OBESIDADE GRAVE
'''

def calcular_imc(altura_em_cm, peso):
    # imc = peso / altura²
    altura = altura_em_cm/100
    imc = peso / (altura * altura) # altura**2
    print(f'SEU IMC: {imc}')
    if imc < 18.5:
        return 'MAGREZA'
    elif imc >= 18.5 and imc <= 24.9:
        return 'NORMAL'
    elif imc >= 25.0 and imc <= 29.9:
        return 'SOBREPESO'
    elif imc >= 30.0 and imc <= 39.9:
        return 'OBESIDADE'
    elif imc > 40.0:
        return 'OBESIDADE GRAVE'
    else:
        'ERRO'

altura = float(input('Digite sua altura em cm: '))
peso = float(input('Digite seu peso: '))
print(calcular_imc(altura, peso))