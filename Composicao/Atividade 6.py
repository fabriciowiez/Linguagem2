class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.salario}"

class Departamento:
    def __init__(self, nome, funcionarios=[]):
        self.nome = nome
        self.funcionarios = funcionarios

    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listaDeFuncionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

f1 = Funcionario("Fabrício", 2000)
f2 = Funcionario("Jonas", 3000)
dep = Departamento("Desenvolvimento")

while 1:
    print("1 - Adicionar funcionários")
    print("2 - Listar funcionários")
    print("0 - Sair")

    opc = int(input("Insira sua opção: "))

    if opc == 1:
        dep.addFuncionario(f1)
        dep.addFuncionario(f2)
    elif opc == 2:        
        dep.listaDeFuncionarios()
    else: break