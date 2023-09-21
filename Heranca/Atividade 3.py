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
    
empregado = Empregado("Fabrício Medeiros Ciechowiez", "Rua 7 de Setembro, 123", 1500, 6)

print(f"Nome do empregado: {empregado.getNome()}")
print(f"Endereço do empregado: {empregado.getEndereco()}")
print(f"Salário Base: {empregado.salarioBase}")
print(f"Meses Trablhados: {empregado.mesesTrabalhados}")
print(f"Salário: {empregado.calcularSalario()}")