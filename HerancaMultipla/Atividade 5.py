class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibeDados(self):
        print(f"Nome do funcionario: {self.nome}")
        print(f"Salario do funcionario: {self.salario}")

class Gerente():
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def exibeDados(self):
        print(f"Nome do gerente: {self.nome}")
        print(f"Salario do gerente: {self.salario}")
        print(f"Departamento: {self.departamento}")

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.getMatricula()}")

class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus_salarial):
        super().__init__(nome, salario, matricula)
        self.bonus_salarial = bonus_salarial

    def exibeDados(self):
        super().exibeDados()
        print(f"Bônus: {self.bonus_salarial}")

class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, add_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.add_noturno = add_noturno
    
    def exibeDados(self):
        super().exibeDados()
        print(f"Turno: {self.turno}")
        print(f"Adicional noturno: {self.add_noturno}")

funcionario = Funcionario("Fabrício", 2500)
funcionario.exibeDados()

gerente = Gerente("Ober", 5000, "Contabilidade")
gerente.exibeDados()

assistente = Assistente("Fa", 2000, 495)
assistente.exibeDados()

assistTecnico = Tecnico("Messi", 3000, 386, 500)
assistTecnico.exibeDados()

assistAdm = Administrativo("Cristiano", 3500, 231, 600, 100)
assistAdm.exibeDados()