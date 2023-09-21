class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def getNome(self):
        return self.nome
    
    def getEndereco(self):
        return self.endereco
    
    def setNome(self, nome):
        self.nome = nome
    
    def setEndereco(self, endereco):
        self.endereco = endereco

class Empregado(Pessoa):
    def __init__(self, nome, endereco, salarioBase, mesesTrabalhados):
        super().__init__(nome, endereco)
        self.salarioBase = salarioBase
        self.mesesTrabalhados = mesesTrabalhados

    def calcularSalario(self):
        return self.salarioBase * self.mesesTrabalhados
    
class Administrador(Empregado):
    def __init__(self, nome, endereco, salarioBase, mesesTrabalhados, ajudasDeCusto):
        super().__init__(nome, endereco, salarioBase, mesesTrabalhados)
        self.ajudasDeCusto = ajudasDeCusto

    def calcularSalario(self):
        salario_base = super().calcularSalario()
        return salario_base + self.ajudasDeCusto

adm = Administrador("Fabrício Medeiros Ciechowiez", "Rua 7 de Setembro, 123", 1500, 6, 1000)

print(f"Nome do empregado: {adm.getNome()}")
print(f"Endereço do empregado: {adm.getEndereco()}")
print(f"Salário Base: {adm.salarioBase}")
print(f"Meses Trabalhados: {adm.mesesTrabalhados}")
print(f"Ajudas de Custo: {adm.ajudasDeCusto}")
print(f"Salário com as ajudas de custo: {adm.calcularSalario()}")
