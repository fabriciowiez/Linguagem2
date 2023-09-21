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
    
class Operario(Empregado):
    def __init__(self, nome, endereco, salarioBase, mesesTrabalhados, valorProducao, comissao):
        super().__init__(nome, endereco, salarioBase, mesesTrabalhados)
        self.valorProducao = valorProducao
        self.comissao = comissao

    def calcularSalario(self):
        salario_base = super().calcularSalario()
        return salario_base + self.comissao

ope = Operario("Fabrício Medeiros Ciechowiez", "Rua 7 de Setembro, 123", 1500, 6, 2500, 1753)

print(f"Nome do empregado: {ope.getNome()}")
print(f"Endereço do empregado: {ope.getEndereco()}")
print(f"Salário Base: {ope.salarioBase}")
print(f"Meses Trabalhados: {ope.mesesTrabalhados}")
print(f"Valor de Produção: {ope.valorProducao}")
print(f"Comissão: {ope.comissao}")
print(f"Salário: {ope.calcularSalario()}")
