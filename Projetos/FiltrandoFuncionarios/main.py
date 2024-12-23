'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

tem_carro_noite = set(set(turno_noite) & set(tem_carro)) # pode ser feito -> set(tem_carro).intersection(turno_noite)
print(tem_carro_noite)

tem_carro_dia = set(set(tem_carro) & set(turno_dia)) # pode ser feito -> set(tem_carro).intersection(turno_dia)
print(tem_carro_dia)

nao_tem_carro = set(set(funcionarios) - set(tem_carro)) # pode ser feito -> set(funcionarios).difference(tem_carro)
print(nao_tem_carro)