from datetime import datetime

class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento): # criando um construtor -> self sempre deve ser passado
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)
    
    def idade(self):
        anoAtual = datetime.now().year
        return anoAtual - int(self.ano_nascimento)

func1 = Funcionarios('Ricardo', 'Duarte', '1999')
func2 = Funcionarios('Glenda', 'Lima', '2001') # é 1999, eu sei

# func1.nome = 'Ricardo'
# func1.ano_nascimento = '1999'
# func2.nome = 'Glenda'
# func2.ano_nascimento = '1999'

# print(func1.nome, func1.ano_nascimento)
# print(func2.nome, func2.ano_nascimento)

# print(func1.nome_completo())
print(Funcionarios.nome_completo(func1))
print(Funcionarios.idade(func1))
# print(func2.nome_completo())
print(Funcionarios.nome_completo(func2))
print(Funcionarios.idade(func2))