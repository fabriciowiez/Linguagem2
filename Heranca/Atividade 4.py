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
    
class Cliente(Pessoa):
    def __init__(self, nome, endereco, credimaximo, valorEmDivida):
        super().__init__(nome, endereco)
        self.credimaximo = credimaximo
        self.valorEmDivida = valorEmDivida

    def obterSaldo(self):
        return self.credimaximo - self.valorEmDivida
    
cliente = Cliente("Fabrício Medeiros Ciechowiez", "Rua 7 de Setembro, 123", 2500, 1650)

print(f"Nome do empregado: {cliente.getNome()}")
print(f"Endereço do empregado: {cliente.getEndereco()}")
print(f"Crédito máximo: {cliente.credimaximo}")
print(f"Valor em dívida: {cliente.valorEmDivida}")
print(f"Saldo: {cliente.obterSaldo()}")