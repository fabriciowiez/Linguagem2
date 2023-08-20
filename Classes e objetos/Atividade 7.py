class Empregado:
    def __init__ (self, nome, departamento, horasTrabalhadasnoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasnoMes = horasTrabalhadasnoMes
        self.salarioPorHora = salarioPorHora

    def mostraDados(self):
        print(f"{self.nome} - {self.departamento} - {self.horasTrabalhadasnoMes} - {self.salarioPorHora}")

    def calculaSalarioMensal(self):
        return self.horasTrabalhadasnoMes * self.salarioPorHora
    
nome = str(input("Informe o nome do empregado: "))
departamento = str(input("Informe o departamento do empregado: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas por mês: "))
salarioHora = float(input("Informe o salário por hora do empregado: "))

e = Empregado(nome, departamento, horasTrabalhadas, salarioHora)

e.mostraDados()

print(f"Salario do empregado: {e.calculaSalarioMensal()}")